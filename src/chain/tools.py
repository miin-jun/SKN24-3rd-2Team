import re
import json
from langchain.tools import tool
from src.crawling import openf1
from src.crawling import ergast
from datetime import datetime
from src.retriever.rag_pipeline import rag_invoke

year = datetime.now().year

def sanitize(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8', errors='ignore').decode('utf-8')
    elif isinstance(obj, dict):
        return {k: sanitize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize(i) for i in obj]
    return obj

@tool
def get_live_race(query: str) -> str:
    """실시간 레이스 정보가 필요할 때 사용"""
    data = openf1.get_live_data()
    return json.dumps(sanitize(data), ensure_ascii=False).encode('utf-8', errors='ignore').decode('utf-8')


@tool
def get_past_race(query: str) -> str:
    """과거 레이스 기록, 드라이버, 팀 정보가 필요할 때 사용"""
    match = re.search(r'20\d{2}', query)
    target_year = int(match.group()) if match else year

    data = {
        "driver_standings": ergast.get_driver_standings(target_year),
        "constructor_standings": ergast.get_constructor_standings(target_year),
    }
    return json.dumps(sanitize(data), ensure_ascii=False)

@tool
def get_round_race(query: str, round: int) -> str:
    """특정 라운드의 레이스 결과, 퀄리파잉, 피트스탑 상세 데이터가 필요할 때 사용.
    특정 그랑프리 우승자, 결과, 순위가 필요할 때 반드시 이 툴을 사용할 것.
    (예시) 호주 그랑프리 결과, 일본 그랑프리 우승자
    """
    match = re.search(r'20\d{2}', query)
    target_year = int(match.group()) if match else year
    data = ergast.get_round_data(target_year, round)
    return json.dumps(sanitize(data), ensure_ascii=False).encode('utf-8', errors='ignore').decode('utf-8')

@tool
def search_regulations(query: str) -> str:
    """F1 규정 설명이 필요할 때 사용"""
    response = rag_invoke(query)
    return str(response["answer"]).encode('utf-8', errors='ignore').decode('utf-8')