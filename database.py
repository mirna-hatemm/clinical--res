import mysql.connector

db = mysql.connector.connect(
    host="mysql-container",
    user="root",
    password="root",
    database="user"
)


def get_cursor():
    return db.cursor()


def commit():
    try:
        db.commit()
        print("Changes committed successfully.")
    except Exception as e:
        db.rollback()
        print("Error occurred during commit. Changes rolled back.")
        print("Error message:", str(e))

