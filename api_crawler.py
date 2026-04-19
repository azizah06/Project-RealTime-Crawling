import requests
from datetime import datetime
from db import collection
from config import API_KEY

def crawl_news_mbg():
    url = "https://newsapi.org/v2/everything"

    topics = [
    "MBG Indonesia",
    "MBG kebijakan",
    "MBG pemerintah",
    "MBG terbaru",
    "MBG berita",
    "MBG kontroversi",
    "MBG ekonomi",
    "MBG politik"
]

    for topic in topics:
        params = {
            "q": topic,
            "sortBy": "publishedAt",
            "pageSize": 50,
            "apiKey": API_KEY
        }

        try:
            res = requests.get(url, params=params, timeout=10)

            if res.status_code != 200:
                print("ERROR API:", res.status_code)
                continue

            data = res.json()

            print(f"TOPIK: {topic} | JUMLAH:", len(data.get("articles", [])))

            for article in data.get("articles", []):
                title = article.get("title")

                if not title:
                    continue

                doc = {
                    "title": title,
                    "content": article.get("description"),
                    "source": "NEWS_API",
                    "platform": "NEWS",
                    "topic": "MBG_INDONESIA",
                    "url": article.get("url"),
                    "timestamp": datetime.utcnow()
                }

                collection.update_one(
                    {"title": title},
                    {"$setOnInsert": doc},
                    upsert=True
                )

                print("INSERT NEWS:", title)

        except Exception as e:
            print("ERROR NEWS:", e)

    print("✔ Data berita MBG Indonesia masuk")