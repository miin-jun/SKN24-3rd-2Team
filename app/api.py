from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from app.main import agent
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9)) # 한국 시각

app = FastAPI()

class Query(BaseModel):
    question: str

# @app.post("/ask")
# def ask(query: Query):
#     result = agent.invoke({"messages": [HumanMessage(content=query.question)]})
#     for msg in result["messages"]:
#         print(type(msg).__name__, "|", str(msg.content)[:200])
#     answer = result["messages"][-1].content
#     answer = str(answer).encode("utf-8", errors="ignore").decode("utf-8")
#     return {"answer": answer}

@app.post("/ask")
def ask(query: Query):
    now = datetime.now(KST)
    question_with_date = f"[오늘 날짜: {now.strftime('%Y년 %m월 %d일')}]\n{query.question}"
    result = agent.invoke({"messages": [HumanMessage(content=question_with_date)]})
    for msg in result["messages"]:
        print(type(msg).__name__, "|", str(msg.content)[:200])
    answer = result["messages"][-1].content
    answer = str(answer).encode("utf-8", errors="ignore").decode("utf-8")
    return {"answer": answer}