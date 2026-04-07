import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from src.chain.agent import llm, tools
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9)) # 한국 시각
now = datetime.now(KST)

PROMPT = """당신은 F1 전문 챗봇입니다.
오늘 날짜: {now.strftime('%Y년 %m월 %d일')}
사용자의 질문에 따라 적절한 도구를 선택해 답변하세요.
답변은 한국어로만 하세요.
규정 관련: search_regulations
현재 실시간 레이스 관련: get_live_race
과거 시즌 기록: get_past_race
특정 라운드 기록: get_round_race
"""

# agent = create_react_agent(llm, tools, prompt=PROMPT)

# def sanitize(text: str) -> str:
#     return text.encode('utf-8', errors='ignore').decode('utf-8')

def run():
    agent = create_react_agent(llm, tools, prompt=PROMPT)
    
    print("🏎️ F1 설명 챗봇 시작 (종료: exit)\n")
    messages = []

    while True:
        query = input("질문: ").strip()

        if not query:
            continue
        if query.lower() == "exit":
            print("종료합니다.")
            break

        messages.append(HumanMessage(content=query))
        # result = agent.invoke({"messages": messages})
        # answer = result["messages"][-1].content
        # print(f"\n답변: {answer}\n")
        # messages = result["messages"]

        result = agent.invoke({"messages": messages})
        answer = result["messages"][-1].content
        answer = answer.encode('utf-8', errors='ignore').decode('utf-8')
        print(f"\n답변: {answer}\n")

        # 히스토리 sanitize
        messages = result["messages"]
        for msg in messages:
            if isinstance(msg.content, str):
                msg.content = msg.content.encode('utf-8', errors='ignore').decode('utf-8')
            elif isinstance(msg.content, list):
                for block in msg.content:
                    if isinstance(block, dict) and "text" in block:
                        block["text"] = block["text"].encode('utf-8', errors='ignore').decode('utf-8')

if __name__ == "__main__":
    run()