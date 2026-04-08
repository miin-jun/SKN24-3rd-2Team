from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from app.main import agent

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    result = agent.invoke({"messages": [HumanMessage(content=query.question)]})
    for msg in result["messages"]:
        print(type(msg).__name__, "|", str(msg.content)[:200])
    answer = result["messages"][-1].content
    answer = str(answer).encode("utf-8", errors="ignore").decode("utf-8")
    return {"answer": answer}