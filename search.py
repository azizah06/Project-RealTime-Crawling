from db import collection

def search_data(keyword):
    results = collection.find({
        "$text": {"$search": keyword}
    })

    print(f"\nHASIL PENCARIAN: {keyword}\n")

    for r in results:
        print("-", r["title"])


if __name__ == "__main__":
    search_data("MBG")