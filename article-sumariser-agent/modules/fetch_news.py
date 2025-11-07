import requests
from typing import List, Dict
from config.settings import NEWSAPI_KEY

NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"

def get_top_articles(query: str, count: int = 5, language: str = "en") -> List[Dict]:
    if not NEWSAPI_KEY:
        raise RuntimeError("NEWSAPI_KEY not configured. Set it in your .env")
    params = {"q": query, "apiKey": NEWSAPI_KEY, "pageSize": max(count * 2, 10), "language": language}
    resp = requests.get(NEWSAPI_ENDPOINT, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    articles = data.get("articles", [])
    return articles[:count]
