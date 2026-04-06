from langchain_openai import ChatOpenAI
from src.chain.tools import get_live_race, get_past_race, get_round_race, search_regulations

tools = [
    search_regulations,
    get_live_race,
    get_past_race,
    get_round_race
]

llm = ChatOpenAI(model="gpt-4o-mini") # 임의로 선정