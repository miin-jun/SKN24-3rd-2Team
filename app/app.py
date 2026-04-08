# import os
# import sys
# from pathlib import Path

# import streamlit as st
# from langchain_chroma import Chroma
# from langchain_core.embeddings import Embeddings
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate

# APP_DIR = Path(__file__).resolve().parent
# REPO_ROOT = APP_DIR.parent

# if str(REPO_ROOT) not in sys.path:
#     sys.path.insert(0, str(REPO_ROOT))
# # =========================
# # 기본 설정
# # =========================
# st.set_page_config(
#     page_title="For every1",
#     page_icon="🏎️",
#     layout="centered",
# )

# BASE_DIR = REPO_ROOT
# LOGO_PATH = APP_DIR / "logo.png"
# VECTOR_DIR = str(REPO_ROOT / "vectorstore" / "chroma_f1_e5")
# COLLECTION_NAME = "f1_rules_e5"
# TOP_K = 4

# PROMPT_SYSTEM = """
# 당신은 F1 전문 챗봇입니다.

# 규칙:
# 1. 답변은 한국어로만 합니다.
# 2. 제공된 context를 가장 우선적으로 사용합니다.
# 3. context에 없는 내용은 추측하지 말고, 모르면 모른다고 말합니다.
# 4. 초보자도 이해하기 쉽게 설명합니다.
# 5. 보통 3~6문장 정도로 답합니다.
# 6. 필요한 경우 규정, 용어, 판정 맥락을 쉽게 풀어서 설명합니다.
# """.strip()

# # =========================
# # 스타일
# # =========================
# st.markdown("""
# <style>
# @import url('https://cdn.jsdelivr.net/gh/sunn-us/SUIT/fonts/static/woff2/SUIT.css');

# html, body, [class*="css"] {
#     font-family: "SUIT", "Pretendard", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
# }

# .stApp {
#     background: #ffffff;
# }

# .block-container {
#     max-width: 860px;
#     padding-top: 1.4rem;
#     padding-bottom: 2rem;
# }

# .logo-wrap {
#     text-align: center;
#     margin-bottom: 1.2rem;
# }

# .logo-title {
#     text-align: center;
#     font-size: 1.85rem;
#     font-weight: 800;
#     color: #111111;
#     letter-spacing: -0.03em;
#     margin-top: 0.95rem;
#     margin-bottom: 0.1rem;
#     line-height: 1.32;
# }

# .top-bar {
#     display: flex;
#     justify-content: flex-end;
#     margin-bottom: 0.9rem;
# }

# div.stButton > button {
#     border-radius: 999px;
#     border: 1px solid #e3e3e3;
#     background: #ffffff;
#     color: #222222;
#     font-weight: 600;
#     padding: 0.42rem 0.85rem;
#     box-shadow: none;
# }

# div.stButton > button:hover {
#     border-color: #cfcfcf;
#     color: #111111;
#     background: #fafafa;
# }

# div[data-testid="stChatMessage"] {
#     padding-top: 0.35rem;
#     padding-bottom: 0.35rem;
# }

# div[data-testid="stChatMessageContent"] {
#     border-radius: 22px;
#     padding: 1rem 1.08rem;
#     font-size: 1rem;
#     line-height: 1.82;
#     box-shadow: none;
# }

# [data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) div[data-testid="stChatMessageContent"] {
#     background: #ffffff;
#     border: 1px solid #ebebeb;
#     color: #111111;
# }

# [data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) div[data-testid="stChatMessageContent"] {
#     background: #ffffff;
#     border: 1px solid #dddddd;
#     color: #111111;
# }

# div[data-testid="stChatInput"] {
#     border-radius: 999px !important;
#     background: #ffffff !important;
#     border: 1px solid #e5e5e5 !important;
# }

# div[data-testid="stChatInput"] textarea,
# div[data-testid="stChatInput"] input {
#     font-size: 1rem !important;
#     color: #111111 !important;
# }

# .small-fallback {
#     text-align: center;
#     font-size: 2.6rem;
#     font-weight: 900;
#     color: #222222;
#     margin-bottom: 0.8rem;
# }

# header[data-testid="stHeader"] {
#     background: rgba(255, 255, 255, 0);
# }

# [data-testid="stBottomBlockContainer"] {
#     background: #ffffff;
# }
# </style>
# """, unsafe_allow_html=True)

# # =========================
# # 유틸
# # =========================
# def sanitize(text: str) -> str:
#     if text is None:
#         return ""
#     return str(text).encode("utf-8", errors="ignore").decode("utf-8")


# def normalize_answer_content(content) -> str:
#     if isinstance(content, str):
#         return sanitize(content)

#     if isinstance(content, list):
#         parts = []
#         for block in content:
#             if isinstance(block, dict) and "text" in block:
#                 parts.append(str(block["text"]))
#             else:
#                 parts.append(str(block))
#         return sanitize("\n".join(parts).strip())

#     return sanitize(str(content))


# def format_chat_history(messages: list[dict]) -> str:
#     lines = []
#     for msg in messages:
#         role = "사용자" if msg["role"] == "user" else "챗봇"
#         lines.append(f"{role}: {msg['content']}")
#     return "\n".join(lines)


# def build_context(docs) -> str:
#     context_blocks = []

#     for i, doc in enumerate(docs, start=1):
#         metadata = doc.metadata or {}
#         source = metadata.get("source", "")
#         doc_type = metadata.get("doc_type", "")
#         clause = metadata.get("Clause", "")

#         header_parts = [f"[문서 {i}]"]
#         if source:
#             header_parts.append(f"source={source}")
#         if doc_type:
#             header_parts.append(f"type={doc_type}")
#         if clause:
#             header_parts.append(f"clause={clause}")

#         header = " | ".join(header_parts)
#         context_blocks.append(f"{header}\n{doc.page_content}")

#     return "\n\n---\n\n".join(context_blocks)


# # =========================
# # 리소스 로드
# # =========================
# @st.cache_resource(show_spinner=False)
# def load_llm():
#     # 기존 프로젝트 LLM 재사용
#     from src.chain.agent import llm
#     return llm


# # @st.cache_resource(show_spinner=False)
# # def load_vectorstore():
# #     import torch

# #     device = "cuda" if torch.cuda.is_available() else "cpu"

# #     embeddings = HuggingFaceEmbeddings(
# #         model_name="intfloat/multilingual-e5-large",
# #         model_kwargs={"device": device},
# #         encode_kwargs={
# #             "normalize_embeddings": True,
# #             "prompt": "passage: ",
# #         },
# #     )

# #     vector_store = Chroma(
# #         persist_directory=VECTOR_DIR,
# #         collection_name=COLLECTION_NAME,
# #         embedding_function=embeddings,
# #     )
# #     return vector_store
# @st.cache_resource(show_spinner=False)
# def load_vectorstore():
#     from src.retriever.rag_pipeline import retriever
#     return retriever.vectorstore

# # =========================
# # RAG 답변
# # =========================
# def rag_answer(user_prompt: str, messages: list[dict]) -> str:
#     if not os.path.exists(VECTOR_DIR):
#         return (
#             "벡터DB 폴더를 찾지 못했어요.\n\n"
#             f"- 확인 경로: {VECTOR_DIR}\n"
#             "- 먼저 `python build_db.py`로 벡터DB를 생성한 뒤 다시 실행해주세요."
#         )

#     try:
#         llm = load_llm()
#         vector_store = load_vectorstore()

#         # retrieval
#         retrieved_docs = vector_store.similarity_search(user_prompt, k=TOP_K)

#         context = build_context(retrieved_docs)
#         chat_history = format_chat_history(messages[:-1])

#         prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", PROMPT_SYSTEM),
#                 (
#                     "human",
#                     """이전 대화:
# {chat_history}

# 참고 context:
# {context}

# 사용자 질문:
# {question}

# 위 context를 바탕으로 답변해주세요."""
#                 ),
#             ]
#         )

#         # generation
#         chain = prompt | llm | StrOutputParser()

#         answer = chain.invoke(
#             {
#                 "chat_history": chat_history if chat_history else "이전 대화 없음",
#                 "context": context if context else "검색된 문서 없음",
#                 "question": user_prompt,
#             }
#         )

#         answer = normalize_answer_content(answer).strip()

#         if not answer:
#             return "관련 내용을 찾았지만 응답을 생성하지 못했어요. 질문을 조금 더 구체적으로 바꿔서 다시 물어봐 주세요."

#         return answer

#     except Exception as e:
#         traceback.print_exc() 
#         return f"응답 생성 중 오류가 발생했어요: {sanitize(str(e))}"


# def handle_prompt(prompt: str):
#     prompt = sanitize(prompt).strip()
#     if not prompt:
#         return

#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.spinner("답변 생성 중..."):
#         answer = rag_answer(prompt, st.session_state.messages)

#     st.session_state.messages.append({"role": "assistant", "content": answer})


# # =========================
# # 세션 상태
# # =========================
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": "안녕하세요! For every1입니다. 궁금한 F1 규정, 경기, 용어를 편하게 물어보세요."
#         }
#     ]


# # =========================
# # 상단
# # =========================
# st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)

# if LOGO_PATH.exists():
#     c1, c2, c3 = st.columns([1, 3.2, 1])
#     with c2:
#         st.image(str(LOGO_PATH), use_container_width=True)
# else:
#     st.markdown('<div class="small-fallback">For every1</div>', unsafe_allow_html=True)

# st.markdown(
#     '<div class="logo-title">F1을 더 쉽게 이해하는 대화형 챗봇</div>',
#     unsafe_allow_html=True
# )
# st.markdown('</div>', unsafe_allow_html=True)

# st.markdown('<div class="top-bar">', unsafe_allow_html=True)
# if st.button("대화 초기화"):
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": "대화가 초기화되었습니다. 다시 질문해주세요!"
#         }
#     ]
#     st.rerun()
# st.markdown('</div>', unsafe_allow_html=True)

# # =========================
# # 채팅
# # =========================
# for msg in st.session_state.messages:
#     avatar = "🤍" if msg["role"] == "assistant" else "🙂"
#     with st.chat_message(msg["role"], avatar=avatar):
#         st.markdown(msg["content"])

# # =========================
# # 입력
# # =========================
# if prompt := st.chat_input("예: 트랙 리밋은 언제 페널티가 돼?"):
#     handle_prompt(prompt)
#     st.rerun()



import os
import sys
from pathlib import Path

import requests
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="For every1",
    page_icon="🏎️",
    layout="centered",
)

LOGO_PATH = APP_DIR / "logo.png"

# =========================
# 스타일
# =========================
st.markdown("""
<style>
@import url('https://cdn.jsdelivr.net/gh/sunn-us/SUIT/fonts/static/woff2/SUIT.css');

html, body, [class*="css"] {
    font-family: "SUIT", "Pretendard", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}

.stApp {
    background: #ffffff;
}

.block-container {
    max-width: 860px;
    padding-top: 1.4rem;
    padding-bottom: 2rem;
}

.logo-wrap {
    text-align: center;
    margin-bottom: 1.2rem;
}

.logo-title {
    text-align: center;
    font-size: 1.85rem;
    font-weight: 800;
    color: #111111;
    letter-spacing: -0.03em;
    margin-top: 0.95rem;
    margin-bottom: 0.1rem;
    line-height: 1.32;
}

.top-bar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 0.9rem;
}

div.stButton > button {
    border-radius: 999px;
    border: 1px solid #e3e3e3;
    background: #ffffff;
    color: #222222;
    font-weight: 600;
    padding: 0.42rem 0.85rem;
    box-shadow: none;
}

div.stButton > button:hover {
    border-color: #cfcfcf;
    color: #111111;
    background: #fafafa;
}

div[data-testid="stChatMessage"] {
    padding-top: 0.35rem;
    padding-bottom: 0.35rem;
}

div[data-testid="stChatMessageContent"] {
    border-radius: 22px;
    padding: 1rem 1.08rem;
    font-size: 1rem;
    line-height: 1.82;
    box-shadow: none;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) div[data-testid="stChatMessageContent"] {
    background: #ffffff;
    border: 1px solid #ebebeb;
    color: #111111;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) div[data-testid="stChatMessageContent"] {
    background: #ffffff;
    border: 1px solid #dddddd;
    color: #111111;
}

div[data-testid="stChatInput"] {
    border-radius: 999px !important;
    background: #ffffff !important;
    border: 1px solid #e5e5e5 !important;
}

div[data-testid="stChatInput"] textarea,
div[data-testid="stChatInput"] input {
    font-size: 1rem !important;
    color: #111111 !important;
}

.small-fallback {
    text-align: center;
    font-size: 2.6rem;
    font-weight: 900;
    color: #222222;
    margin-bottom: 0.8rem;
}

header[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0);
}

[data-testid="stBottomBlockContainer"] {
    background: #ffffff;
}
</style>
""", unsafe_allow_html=True)


# =========================
# 유틸
# =========================
def sanitize(text: str) -> str:
    if text is None:
        return ""
    return str(text).encode("utf-8", errors="ignore").decode("utf-8")


# =========================
# API 호출
# =========================
def agent_answer(user_prompt: str) -> str:
    try:
        res = requests.post(
            "http://localhost:8000/ask",
            json={"question": user_prompt},
            timeout=120,
        )
        return sanitize(res.json()["answer"])
    except Exception as e:
        return f"응답 생성 중 오류가 발생했어요: {sanitize(str(e))}"


def handle_prompt(prompt: str):
    prompt = sanitize(prompt).strip()
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("답변 생성 중..."):
        answer = agent_answer(prompt)

    st.session_state.messages.append({"role": "assistant", "content": answer})


# =========================
# 세션 상태
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! For every1입니다. 궁금한 F1 규정, 경기, 용어를 편하게 물어보세요."
        }
    ]


# =========================
# 상단
# =========================
st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)

if LOGO_PATH.exists():
    c1, c2, c3 = st.columns([1, 3.2, 1])
    with c2:
        st.image(str(LOGO_PATH), use_container_width=True)
else:
    st.markdown('<div class="small-fallback">For every1</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="logo-title">F1을 더 쉽게 이해하는 대화형 챗봇</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="top-bar">', unsafe_allow_html=True)
if st.button("대화 초기화"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "대화가 초기화되었습니다. 다시 질문해주세요!"
        }
    ]
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 채팅
# =========================
for msg in st.session_state.messages:
    avatar = "🤍" if msg["role"] == "assistant" else "🙂"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# =========================
# 입력
# =========================
if prompt := st.chat_input("예: 트랙 리밋은 언제 페널티가 돼?"):
    handle_prompt(prompt)
    st.rerun()