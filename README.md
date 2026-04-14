# 🎬 Movie Recommendation System (Full-Stack)

A **full-stack Movie Recommendation System** inspired by Netflix, built using **Machine Learning (Collaborative Filtering)** and a **Flask + HTML/CSS/JavaScript architecture**.

This project allows users to:
- 🔐 Register & Login  
- 🎯 Get personalized movie recommendations  
- 🕒 View their watch history  
- 🌐 Interact through a web-based UI  

---

## 🚀 Features

- 🔐 **User Authentication** (Register/Login)
- 🎬 **Movie Recommendations** using Collaborative Filtering
- 🧠 **Cosine Similarity Algorithm**
- 🕒 **User History Tracking**
- 🌑 Netflix-style **dark UI**
- ⚡ Fast API-based communication (Frontend ↔ Backend)
- 🗄️ SQLite database integration

---

## 🧠 Algorithm Used

### 📌 Collaborative Filtering (Item-Based)

- Recommends movies based on similarity between items  
- Uses **Cosine Similarity** to find similar movies  

👉 Idea:
> If users who liked Movie A also liked Movie B, then recommend Movie B.

---

## 🛠️ Tech Stack

### 🔹 Frontend
- HTML  
- CSS  
- JavaScript  

### 🔹 Backend
- Python  
- Flask  
- Flask-CORS  

### 🔹 Machine Learning
- Scikit-learn  
- Pandas  
- NumPy  

### 🔹 Database
- SQLite  

---


## 📥 Dataset

This project uses the **MovieLens Dataset**.

Required files:
- `movies.csv`
- `ratings.csv`

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Manojs018/MovieRecomendationSystem.git
cd movie-recommender

###  Setup Backend
cd backend
pip install -r requirements.txt
python app.py

Frontend (HTML/JS)
        ↓
Fetch API Requests
        ↓
Flask Backend (REST API)
        ↓
Machine Learning Model
        ↓
SQLite Database (User + History)
        ↓
Response → Frontend UI

| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| GET    | /movies         | Get movie list      |
| POST   | /register       | Register user       |
| POST   | /login          | Login user          |
| POST   | /recommend      | Get recommendations |
| GET    | /history/<user> | Get user history    |

