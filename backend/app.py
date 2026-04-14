from flask import Flask, request, jsonify
import pandas as pd
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to connect

# ================= DATABASE =================
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    movie TEXT
)
''')
conn.commit()

# ================= ML MODEL =================
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

data = pd.merge(ratings, movies, on='movieId')

matrix = data.pivot_table(index='userId', columns='title', values='rating').fillna(0)
similarity = cosine_similarity(matrix.T)

similarity_df = pd.DataFrame(similarity,
                            index=matrix.columns,
                            columns=matrix.columns)

# ================= ROUTES =================

@app.route('/movies', methods=['GET'])
def movies_list():
    return jsonify(list(similarity_df.columns))

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (data['username'], data['password']))
        conn.commit()
        return jsonify({"message": "Registered successfully"})
    except:
        return jsonify({"error": "User exists"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (data['username'], data['password']))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid credentials"})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie = data['movie']
    username = data['username']

    similar = similarity_df[movie].sort_values(ascending=False)
    recs = list(similar.iloc[1:6].index)

    # save history
    cursor.execute("INSERT INTO history (username, movie) VALUES (?, ?)",
                   (username, movie))
    conn.commit()

    return jsonify({"recommendations": recs})

@app.route('/history/<username>', methods=['GET'])
def history(username):
    cursor.execute("SELECT movie FROM history WHERE username=?", (username,))
    rows = cursor.fetchall()
    return jsonify([r[0] for r in rows])

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)