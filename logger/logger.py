import time
import mysql.connector
from pymongo import MongoClient


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


mongo_client = MongoClient("mongodb://mongo/")
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