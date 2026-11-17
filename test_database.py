import sqlite3


connection = sqlite3.connect("archive.db")

connection.row_factory = sqlite3.Row

cursor = connection.cursor()


consoles = cursor.execute("""
SELECT *
FROM consoles
""").fetchall()


for console in consoles:
    print(
        console["id"],
        console["slug"],
        console["name"],
        console["theme"]
    )


connection.close()