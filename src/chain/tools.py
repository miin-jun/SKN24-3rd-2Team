import re
from langchain.tools import tool
from src.crawling import openf1
from src.crawling import ergast
from datetime import datetime
from src.retriever.rag_pipeline import rag_invoke

year = datetime.now().year

@tool
def get_live_race(query: str) -> str:
    """실시간 레이스 정보가 필요할 때 사용"""
    data = openf1.get_live_data()
    return str(data).encode('utf-8', errors='ignore').decode('utf-8')

@tool
def get_past_race(query: str) -> str:
    """과거 레이스 기록, 드라이버, 팀 정보가 필요할 때 사용"""
    match = re.search(r'20\d{2}', query)

    if match:
        target_year = int(match.group())
    else:
        target_year = year

    data = ergast.get_season_data(target_year)
    return str(data).encode('utf-8', errors='ignore').decode('utf-8')

@tool
def get_round_race(query: str, round: int) -> str:
    """특정 라운드 상세 데이터가 필요할 때 사용
    (예시) 호주 그랑프리 퀄리파잉 정보
    """
    match = re.search(r'20\d{2}', query)
    
    if match:
        target_year = int(match.group())
    else:
        target_year = year

    data = ergast.get_round_data(target_year, round)
    return str(data).encode('utf-8', errors='ignore').decode('utf-8')

@tool
def search_regulations(query: str) -> str:
    """F1 규정 설명이 필요할 때 사용"""
    response = rag_invoke(query)
    return str(response["answer"]).encode('utf-8', errors='ignore').decode('utf-8')