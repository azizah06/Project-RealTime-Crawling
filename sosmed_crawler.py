from datetime import datetime
from db import collection

import random

def crawl_social_mbg():
    base_tweets = [
        "MBG lagi ramai dibahas",
        "Kebijakan MBG menuai pro kontra",
        "MBG cukup menarik",
        "Netizen membicarakan MBG",
        "MBG trending di Indonesia"
    ]

    tweets = []

    for _ in range(20):  # generate 20 data tiap run
        tweet = random.choice(base_tweets) + f" #{random.randint(1,1000)}"
        tweets.append(tweet)

    print("JUMLAH DATA SOSIAL:", len(tweets))

    for tweet in tweets:
        doc = {
            "title": tweet,
            "content": tweet,
            "source": "SIMULATED_TWITTER",
            "platform": "SOCIAL_MEDIA",
            "topic": "MBG_INDONESIA",
            "url": None,
            "timestamp": datetime.utcnow()
        }

        collection.update_one(
            {"title": tweet},
            {"$setOnInsert": doc},
            upsert=True
        )

        print("INSERT SOCIAL:", tweet)