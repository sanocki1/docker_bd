from flask import Flask, request
import mysql.connector
import os

MYSQL_HOST = os.getenv("MYSQL_HOST", "db")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "wydarzenia")
PASSWORD = os.getenv("WEB_PASSWORD")

if not PASSWORD:
    raise Exception("WEB_PASSWORD env variable not set")
if not MYSQL_PASSWORD:
    raise Exception("DB_PASSWORD env variable not set")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        haslo = request.form["haslo"]
        imie = request.form["imie"]
        wydarzenie = request.form["wydarzenie"]

        if haslo != PASSWORD:
            return "Bledne haslo"

        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

        cursor = db.cursor()

        sql = """
        INSERT INTO zapisy(imie, wydarzenie)
        VALUES (%s, %s)
        """

        values = (imie, wydarzenie)

        cursor.execute(sql, values)

        db.commit()

        cursor.close()
        db.close()

        return "Zapisano!"

    return """
    <h1>Zapisy na wydarzenia</h1>

    <form method="POST">

        Haslo:<br>
        <input type="password" name="haslo"><br><br>

        Imie:<br>
        <input type="text" name="imie"><br><br>

        Wydarzenie:<br>
        <select name="wydarzenie">
            <option>Konferencja</option>
            <option>Warsztaty</option>
            <option>Prezentacja</option>
        </select>

        <br><br>

        <input type="submit">

    </form>
    """

app.run(host="0.0.0.0", port=5000)