# 🚀 Real-Time Big Data Crawling with MongoDB (Replica Set)

## 📌 Deskripsi
Project ini merupakan implementasi pengelolaan Big Data dengan melakukan crawling data dari berbagai sumber dan menyimpannya ke dalam NoSQL database (MongoDB) menggunakan arsitektur Replica Set (distributed system).

Sistem berjalan secara real-time dengan interval tertentu dan mendukung otomasi serta indexing untuk pencarian cepat.

---

## 🎯 Fitur Utama

- 🔄 Crawling data real-time (interval 5 menit)
- 🌐 Sumber data:
  - News API (semi-structured)
  - Simulasi Social Media (unstructured)
- 🗄️ MongoDB NoSQL Database
- 🐳 Docker Container
- 🧩 MongoDB Replica Set (Distributed System)
- ⚡ Indexing untuk pencarian cepat
- 🚫 Anti-duplicate data

---

## 🏗️ Arsitektur Sistem

    [News API] ----\
                    --> [Python Crawler] --> [MongoDB Replica Set]
    [Social Data] --/

---

## 🗂️ Struktur Project

    .
    ├── api_crawler.py
    ├── sosmed_crawler.py
    ├── db.py
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

## 🧾 Struktur Data (MongoDB Document)

    {
      "title": "...",
      "content": "...",
      "source": "NEWS_API / SOCIAL",
      "platform": "NEWS / SOCIAL_MEDIA",
      "topic": "MBG_INDONESIA",
      "url": "...",
      "timestamp": "..."
    }

---

## 🐳 Setup MongoDB dengan Docker (Replica Set)

### 1. Buat network

    docker network create mongo-net

---

### 2. Jalankan container MongoDB

    docker run -d --name mongo1 --network mongo-net -p 27020:27017 mongo --replSet rs0
    docker run -d --name mongo2 --network mongo-net -p 27021:27017 mongo --replSet rs0
    docker run -d --name mongo3 --network mongo-net -p 27022:27017 mongo --replSet rs0

---

### 3. Inisialisasi Replica Set

    docker exec -it mongo1 mongosh

    rs.initiate({
      _id: "rs0",
      members: [
        { _id: 0, host: "mongo1:27017" },
        { _id: 1, host: "mongo2:27017" },
        { _id: 2, host: "mongo3:27017" }
      ]
    })

---

### 4. Cek status

    rs.status()

---

## ⚙️ Setup Project

### 1. Install dependency

    pip install -r requirements.txt

---

### 2. Setup API Key

Buat file `.env`

    API_KEY=your_news_api_key

---

### 3. Jalankan program

    python run.py

---

## 🔄 Cara Kerja Sistem

1. Ambil data dari News API  
2. Generate data sosial (simulasi)  
3. Simpan ke MongoDB  
4. Hindari duplikasi data  
5. Ulangi setiap 5 menit  

---

## ⚡ Indexing

    collection.create_index([("title", "text")])
    collection.create_index("title", unique=True)

---

## 📊 Hasil

- Data tersimpan dalam MongoDB  
- Mendukung pencarian cepat  
- Sistem berjalan otomatis (real-time)  

---

## 🧠 Teknologi

- Python  
- MongoDB  
- Docker  
- PyMongo  
- News API  

---

## 🚀 Pengembangan Selanjutnya

- Sharding untuk scaling data besar  
- Dashboard visualisasi  
- Sentiment analysis  

---

## 👨‍💻 Author

- Nama: (Isi nama kamu)  
- Project: Tugas Big Data  
