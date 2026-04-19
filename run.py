import time
from datetime import datetime
from api_crawler import crawl_news_mbg
from sosmed_crawler import crawl_social_mbg
from db import collection, test_connection, init_db

test_connection()
init_db()

INTERVAL = 120  # 2 menit

def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def run_pipeline():
    try:
        log("Mulai crawling NEWS...")
        crawl_news_mbg()

        log("Mulai crawling SOCIAL...")
        crawl_social_mbg()

        total = collection.count_documents({})
        log(f"TOTAL DATA SAAT INI: {total}")

    except Exception as e:
        log(f"ERROR: {e}")

if __name__ == "__main__":
    log("=== REAL-TIME CRAWLING STARTED ===")

    while True:
        run_pipeline()
        log(f"Menunggu {INTERVAL} detik...\n")
        time.sleep(INTERVAL)