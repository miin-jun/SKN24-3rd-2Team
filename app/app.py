import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from src.chain.agent import llm, tools
from datetime import datetime, timezone, timedelta

# 페이지 설정
st.set_page_config(
    page_title="🏎️ F1 챗봇",
    page_icon="🏎️",
    layout="wide"
)

# 커스텀 CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .chat-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #e10600 0%, #ff1e00 100%);
        color: white;
        border-radius: 0.5rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 헤더
st.markdown("""
    <div class="chat-header">
        <h1>🏎️ F1 전문 챗봇</h1>
        <p>Formula 1 규정, 역사, 레이스 정보를 물어보세요!</p>
    </div>
    """, unsafe_allow_html=True)

# 한국 시각
KST = timezone(timedelta(hours=9))
now = datetime.now(KST)

# 프롬프트
PROMPT = f"""당신은 F1 전문 챗봇입니다.
오늘 날짜: {now.strftime('%Y년 %m월 %d일')}
사용자의 질문에 따라 적절한 도구를 선택해 답변하세요.
답변은 한국어로만 하세요.
규정 관련: search_regulations
현재 실시간 레이스 관련: get_live_race
과거 시즌 기록: get_past_race
특정 라운드 기록: get_round_race
"""

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "agent" not in st.session_state:
    st.session_state.agent = create_react_agent(llm, tools, prompt=PROMPT)


# UTF-8 인코딩 처리 함수
def sanitize(text: str) -> str:
    """UTF-8 인코딩 문제 해결"""
    return text.encode('utf-8', errors='ignore').decode('utf-8')


# 사이드바 - 설정 및 정보
with st.sidebar:
    st.image("https://cdn-1.motorsport.com/images/mgl/YBeAWzX2/s800/f1-logo-1.jpg", width=200)
    
    st.markdown("### 📋 사용 가능한 기능")
    st.markdown("""
    - 🔍 **F1 규정 검색**
    - 🏁 **실시간 레이스 정보**
    - 📊 **과거 시즌 기록**
    - 🎯 **특정 라운드 결과**
    - 📖 **F1 용어 및 역사**
    """)
    
    st.markdown("---")
    
    # 대화 초기화 버튼
    if st.button("🗑️ 대화 초기화", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown(f"**오늘 날짜:** {now.strftime('%Y년 %m월 %d일')}")
    st.markdown(f"**현재 시각:** {now.strftime('%H:%M:%S KST')}")


# 채팅 기록 표시
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    
    with st.chat_message(role):
        st.markdown(content)


# 사용자 입력
if prompt := st.chat_input("F1에 대해 무엇이든 물어보세요..."):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("🏎️ 답변을 생성하는 중..."):
            try:
                # LangChain 메시지 형식으로 변환
                langchain_messages = []
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        langchain_messages.append(HumanMessage(content=msg["content"]))
                    elif msg["role"] == "assistant":
                        langchain_messages.append(AIMessage(content=msg["content"]))
                
                # 에이전트 실행
                result = st.session_state.agent.invoke({"messages": langchain_messages})
                
                # 응답 추출 및 UTF-8 처리
                answer = result["messages"][-1].content
                answer = sanitize(answer)
                
                # 응답 표시
                st.markdown(answer)
                
                # 세션에 저장
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
                # 히스토리 sanitize 처리
                for msg in result["messages"]:
                    if isinstance(msg.content, str):
                        msg.content = sanitize(msg.content)
                    elif isinstance(msg.content, list):
                        for block in msg.content:
                            if isinstance(block, dict) and "text" in block:
                                block["text"] = sanitize(block["text"])
                
            except Exception as e:
                error_msg = f"❌ 오류가 발생했습니다: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})


# 하단 정보
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🔧 사용 기술**")
    st.markdown("- LangChain\n- LangGraph\n- Chroma Vector DB")

with col2:
    st.markdown("**📚 데이터 소스**")
    st.markdown("- FIA 규정\n- F1 용어집\n- 레이스 기록")

with col3:
    st.markdown("**💡 팁**")
    st.markdown("- 구체적인 질문을 해주세요\n- 규정, 기록, 용어 등 다양한 질문 가능")
