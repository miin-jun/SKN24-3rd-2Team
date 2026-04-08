# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import streamlit as st
# from langchain_core.messages import HumanMessage, AIMessage
# from src.chain.agent import llm, tools
# from langgraph.prebuilt import create_react_agent
# from datetime import datetime, timezone, timedelta

# KST = timezone(timedelta(hours=9))
# now = datetime.now(KST)

# PROMPT = f"""당신은 F1 전문 챗봇입니다.
# 오늘 날짜: {now.strftime('%Y년 %m월 %d일')}
# 사용자의 질문에 따라 아래의 도구를 적절하게 선택해 답변하세요.
# 규정 관련: search_regulations
# 현재 실시간 레이스 관련: get_live_race
# 과거 시즌 기록: get_past_race
# 특정 라운드 기록: get_round_race
# 주의사항:
# - 답변은 반드시 한국어로만 하세요.
# - search_regulations의 결과는 수정하거나 재해석하지 말고 그대로 사용자에게 전달하세요.
# - 도구 결과 외의 내용을 추가하거나 보완하지 마세요.
# """

# @st.cache_resource
# def load_agent():
#     return create_react_agent(llm, tools, prompt=PROMPT)

# st.title("🏎️ F1 설명 챗봇")

# agent = load_agent()

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# for role, content in st.session_state.chat_history:
#     with st.chat_message(role):
#         st.write(content)

# if query := st.chat_input("질문을 입력하세요..."):
#     st.session_state.chat_history.append(("user", query))
#     with st.chat_message("user"):
#         st.write(query)

#     with st.chat_message("assistant"):
#         with st.spinner("답변 생성 중..."):
#             result = agent.invoke({"messages": [HumanMessage(content=query)]})
#             answer = result["messages"][-1].content
#             answer = answer.encode('utf-8', errors='ignore').decode('utf-8')
#             st.write(answer)

#     st.session_state.chat_history.append(("assistant", answer))

#     st.session_state.messages = result["messages"]

import requests
import streamlit as st

st.title("🏎️ F1 설명 챗봇")
query = st.text_input("질문을 입력하세요")
if st.button("질문하기"):
    res = requests.post("http://localhost:8000/ask", json={"question": query})
    st.write(res.json()["answer"])