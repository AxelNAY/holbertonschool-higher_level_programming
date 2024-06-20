import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host = "localhost",
            user = username,
            pwd = password,
            db_name = database_name,
            port = 3306
        )
        
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("Error: Data not found.")

    except MySQLdb.Error as error:
        print(f"Error: {error}")