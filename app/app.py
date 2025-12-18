from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()

    if request.method == "POST":
        name = request.form["name"]
        cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()

    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", users=users)



@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    new_name = request.form["name"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name=%s WHERE id=%s",
        (new_name, id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

