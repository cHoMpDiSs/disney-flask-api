from flask import Flask, jsonify, render_template
import psycopg2


app = Flask(__name__)

import os 
from dotenv import load_dotenv

load_dotenv() 

DB_HOST = os.environ.get("HOST")
DB_PORT = os.environ.get("PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("PASSWORD")
DB = os.environ.get("DB")

conn = psycopg2.connect(host=DB_HOST,
                        port=DB_PORT,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        database=DB
                        )


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/comics', methods=['GET'])
def comic_get():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM myapp_comics")
    # Retrieve query results
    records = cur.fetchall()
    items = []
    for item in records:
        items.append(item)
    return render_template("index.html", items=items)

@app.route('/superheros', methods=['GET'])
def super_hero_get():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM myapp_superhero")
    # Retrieve query results
    records = cur.fetchall()
    items = []
    for item in records:
        items.append(item)
    return render_template("index.html", items=items)

@app.route('/toys', methods=['GET'])
def toy_get():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM myapp_toys")
    # Retrieve query results
    records = cur.fetchall()
    items = []
    for item in records:
        items.append(item)
    print(items)
    return render_template("index.html", items=items)





if __name__ == "__main__":
    app.run(host='0.0.0.0')