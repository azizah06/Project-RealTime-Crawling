from db import collection

pipeline = [
    {"$group": {"_id": "$platform", "count": {"$sum": 1}}}
]

for r in collection.aggregate(pipeline):
    print(r)