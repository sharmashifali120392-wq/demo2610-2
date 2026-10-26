import os
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("demo.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    return conn

@app.route("/user")
def get_user():
    name = request.args.get("name", "")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    rows = get_db().execute(query).fetchall()
    return {"rows": rows}

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output

@app.route("/read")
def read_file():
    filename = request.args.get("file", "readme.txt")
    with open(os.path.join("files", filename)) as f:
        return f.read()

@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    return "<h1>Hello " + name + "</h1>"


if __name__ == "__main__":
    # 5) Flask debug mode enabled
    app.run(debug=True)
