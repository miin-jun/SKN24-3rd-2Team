import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from src.chain.agent import llm, tools
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9)) # 한국 시각
now = datetime.now(KST)

PROMPT = f"""당신은 F1 전문 챗봇입니다.
오늘 날짜: {now.strftime('%Y년 %m월 %d일')}

사용자의 질문에 따라 아래의 도구를 적절하게 선택해 답변하세요.
규정 관련: search_regulations
현재 실시간 레이스 관련: get_live_race
과거 시즌 기록, 드라이버 순위, 컨스트럭터 순위, 챔피언십 순위: get_past_race
특정 라운드 기록: get_round_race

주의사항:
- 답변은 반드시 한국어로만 하세요.
- 드라이버 챔피언십 순위나 컨스트럭터 순위는 반드시 get_past_race를 사용하세요.
- search_regulations의 결과는 수정하거나 재해석하지 말고 그대로 사용자에게 전달하세요.
- 도구 결과 외의 내용을 추가하거나 보완하지 마세요.
"""

agent = create_react_agent(llm, tools, prompt=PROMPT)

# def sanitize(text: str) -> str:
#     return text.encode('utf-8', errors='ignore').decode('utf-8')

def run():
    # agent = create_react_agent(llm, tools, prompt=PROMPT)
    
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
        # for msg in messages:
        #     if isinstance(msg.content, str):
        #         msg.content = msg.content.encode('utf-8', errors='ignore').decode('utf-8')
        #     elif isinstance(msg.content, list):
        #         for block in msg.content:
        #             if isinstance(block, dict) and "text" in block:
        #                 block["text"] = block["text"].encode('utf-8', errors='ignore').decode('utf-8')

if __name__ == "__main__":
    run()