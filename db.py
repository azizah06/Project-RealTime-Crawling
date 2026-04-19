from pymongo import MongoClient

client = MongoClient(
    "mongodb://mongo1:27020,mongo2:27021,mongo3:27022/?replicaSet=rs0"
)

db = client["bigdata_db"]
collection = db["data"]

def test_connection():
    print(client.list_database_names())

def init_db():
    # untuk search
    collection.create_index([("title", "text")])
    
    # untuk mencegah duplicate
    collection.create_index("title", unique=True)