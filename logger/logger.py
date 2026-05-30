import time
import mysql.connector
from pymongo import MongoClient

MONGO_URI = "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"

while True:
    try:
        print("Proba MYSQL")
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="logger_pool",
            pool_size=5,
            host="db",
            user="root",
            password="q",
            database="wydarzenia"
        )
        print("OK MYSQL")
        break

    except Exception as err:
        print(err)
        time.sleep(5)

while True:
    try:
        mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        mongo_client.admin.command("ping")
        print("OK MONGO")
        break
    except Exception as err:
        print(err)
        time.sleep(5)

mongo_db = mongo_client["logs_db"]
mongo_collection = mongo_db["audit_logs"]


while True:
    mysql_db = pool.get_connection()
    cursor = mysql_db.cursor(dictionary=True)

    sql = """Select * FROM audit_logs WHERE processed = FALSE"""
    cursor.execute(sql)

    logs = cursor.fetchall()

    for log in logs:

        mongo_collection.insert_one({
            "operation_type": log["operation_type"],
            "description": log["description"],
            "created_at": str(log["created_at"])
        })

        update_cursor = mysql_db.cursor()

        update_cursor.execute("""
            UPDATE audit_logs
            SET processed = TRUE
            WHERE id = %s
        """, (log["id"],))

        mysql_db.commit()

        print("Przeniesiono log:", log["id"])
    mysql_db.close()
    time.sleep(5)