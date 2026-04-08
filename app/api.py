from fastapi import FastAPI
from pydantic import BaseModel
from src.retriever.rag_pipeline import rag_invoke

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    result = rag_invoke(query.question)
    answer = str(result["answer"]).encode("utf-8", errors="ignore").decode("utf-8")
    return {"answer": answer}