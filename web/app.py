from flask import Flask, request
import mysql.connector

app = Flask(__name__)

PASSWORD = "tajne"

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        haslo = request.form["haslo"]
        imie = request.form["imie"]
        wydarzenie = request.form["wydarzenie"]

        if haslo != PASSWORD:
            return "Bledne haslo"

        db = mysql.connector.connect(
            host="db",
            user="root",
            password="q",
            database="wydarzenia"
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