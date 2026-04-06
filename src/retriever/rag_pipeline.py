import os
import torch
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_openai import ChatOpenAI
from sentence_transformers import CrossEncoder
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

hf_token = os.environ.get("HF_TOKEN")
openai_key = os.environ.get("OPENAI_API_KEY")

VECTOR_DIR = "/workspace/SKN24-3rd-2Team/vectorstore/chroma_f1_e5"
MODEL_ID = "google/gemma-3-12b-it"

SYSTEM_MSG = """# SYSTEM RULE
-역할: F1 스포츠 경기 전문 질의응답 시스템
-조건: 사용자가 입문자라고 가정, 쉽고 간단하게 경기 규칙, 용어, 현상을 설명
-제한: context의 내용을 그대로 해석할 것. 
 context에 명시된 조항 번호와 내용을 우선으로 하고,
 절대 context 밖의 지식으로 보완하거나 재해석하지 말 것.(정확한 근거 없는 답변 금지, 유사한 답변을 찾을 수 없는 경우, '현재 데이터베이스에서 찾을 수 없습니다.' 답변)
-언어: 사용자는 한국어 사용자 → 참고문서는 영어이므로 입력된 한국어 질문을 영어로 번역한 후 문서에서 검색, 출력은 한국어 구어체 답변
-사용자의 한국어 구어체의 맥락을 적절히 이해 필요
-친절한 말투로 답변
-F1 기술 용어는 원문 그대로 사용하거나 혹은 정확하게 번역"""


# 모델 로드
def load_embedding_model() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cuda"},
        encode_kwargs={
            "normalize_embeddings": True, 
            "prompt": "passage: "
            },
    )


def load_retriever(embedding_model):
    vector_store = Chroma(
        persist_directory=VECTOR_DIR,
        embedding_function=embedding_model,
        collection_name="f1_rules_e5",
    )
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})

def load_llm() -> HuggingFacePipeline:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.bfloat16,
        device_map="auto",
    )
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.1,
        do_sample=True,
        return_full_text=False,
    )
    return HuggingFacePipeline(pipeline=pipe), tokenizer


# 프롬프트 생성
def build_prompt(question: str, context: str) -> str:
    messages = [
        {
            "role": "user", 
            "content": f"{SYSTEM_MSG}\n\n질문: {question}\n\ncontext:\n{context}\n\n답변:"}
    ]
    return tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

# 컴포넌트 초기화
embedding_model = load_embedding_model()
retriever = load_retriever(embedding_model)
llm, tokenizer = load_llm()
translator = ChatOpenAI(model="gpt-4o-mini", temperature=0)
reranker = CrossEncoder("cross-encoder/mmarco-mMiniLMv2-L12-H384-v1")


def rag_invoke(query: str) -> dict:
    translated = translator.invoke(
        f"Translate to English for F1 regulation search, keep technical terms: {query}"
    ).content

    retrieved = retriever.invoke("query: " + translated)

    pairs = [(translated, doc.page_content) for doc in retrieved]
    scores = reranker.predict(pairs)
    reranked = [doc for _, doc in sorted(zip(scores, retrieved), reverse=True)]

    context = "\n\n".join(doc.page_content for doc in reranked)
    prompt = build_prompt(query, context)
    answer = llm.invoke(prompt)

    return {"answer": answer, "context": reranked}

print("체인 준비 완료")