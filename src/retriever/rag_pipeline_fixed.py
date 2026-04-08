import os
import gc
import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_openai import ChatOpenAI
from sentence_transformers import CrossEncoder

# ── 설정 ───────────────────────────────────────────────
BASE_MODEL = "google/gemma-3-12b-it"
ADAPTER_ID = "YHPark0208/SKN24_3rd_2Team"

SYSTEM_MSG = """# 절대 규칙 (반드시 준수)
- context에 없는 숫자(그리드 페널티, 타이어 세트 수, 시간 제한 등)는 절대 생성 금지. context에 숫자가 없으면 '현재 데이터베이스에서 찾을 수 없습니다'로 답변
- context 외의 지식으로 보완하거나 재해석 금지. 근거 없는 답변 금지
- 규정 문서와 기타 문서 충돌 시 규정 문서 우선. 2026 규정 기준으로 답변
# SYSTEM RULE
-역할: F1 스포츠 경기 전문 질의응답 시스템
-조건: 사용자가 입문자라고 가정, 쉽고 간단하게 경기 규칙, 용어, 현상을 설명
-제한: context의 내용을 그대로 해석할 것.
 context에 명시된 조항 번호와 내용을 우선으로 하고,
 유사한 답변을 찾을 수 없는 경우, '현재 데이터베이스에서 찾을 수 없습니다.' 답변
-언어: 사용자는 한국어 사용자 → 출력은 한국어 구어체 답변
-사용자의 한국어 구어체의 맥락을 적절히 이해 필요
-친절한 말투로 답변
-F1 기술 용어는 원문 그대로 사용하거나 혹은 정확하게 번역"""

# ── 모델 최초 1회 로드 ─────────────────────────────────
print("모델 로딩 중...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
finetuned_model = PeftModel.from_pretrained(base_model, ADAPTER_ID)
print("모델 로드 완료")

# ── 파이프라인 생성 헬퍼 ───────────────────────────────
def make_llm(model):
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.1,
        do_sample=True,
        return_full_text=False
    )
    return HuggingFacePipeline(pipeline=pipe)

# ── RAG 공통 설정 ──────────────────────────────────────
translator = ChatOpenAI(model="gpt-4o-mini", temperature=0)
reranker = CrossEncoder("cross-encoder/mmarco-mMiniLMv2-L12-H384-v1")
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 10}
)

def build_prompt(question: str, context: str) -> str:
    messages = [
        {"role": "user", "content": f"{SYSTEM_MSG}\n\n질문: {question}\n\ncontext:\n{context}\n\n답변:"}
    ]
    return tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

def retrieve_and_rerank(query: str):
    """번역 → 검색 → 리랭킹 (두 모델 공통으로 한 번만 실행)"""
    translated = translator.invoke(
        f"Translate to English for F1 regulation search, keep technical terms: {query}"
    ).content
    retrieved = retriever.invoke("query: " + translated)
    pairs = [(translated, doc.page_content) for doc in retrieved]
    scores = reranker.predict(pairs)
    reranked = [doc for _, doc in sorted(zip(scores, retrieved), reverse=True)]
    return reranked

def rag_invoke(llm, prompt):
    return llm.invoke(prompt)

# ── 비교 함수 ──────────────────────────────────────────
def compare(query: str):
    # 검색/리랭킹은 한 번만
    reranked = retrieve_and_rerank(query)
    context = "\n\n".join(doc.page_content for doc in reranked)
    prompt = build_prompt(query, context)

    # 베이스 모델 응답
    with finetuned_model.disable_adapter():
        base_llm = make_llm(finetuned_model)
        base_answer = rag_invoke(base_llm, prompt)

    # 파인튜닝 모델 응답
    ft_llm = make_llm(finetuned_model)
    ft_answer = rag_invoke(ft_llm, prompt)

    # 출력
    print(f"질문: {query}")
    print("=" * 60)
    print("[베이스 모델]")
    print(base_answer)
    print("=" * 60)
    print("[파인튜닝 모델]")
    print(ft_answer)
    print("=" * 60)
    print("\n참조 문서:")
    for doc in reranked:
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        doc_type = doc.metadata.get("doc_type", "unknown")
        snippet = doc.page_content[:200].replace("\n", " ")
        print(f"- {source} | type: {doc_type} | page: {page} | {snippet}...")
# ── 실행 ───────────────────────────────────────────────
compare("ATR 제한이 어떻게 돼?") 