import sqlite3


DATABASE = "archive.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS sections (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    console_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    content TEXT NOT NULL,

    display_order INTEGER NOT NULL,

    FOREIGN KEY(console_id) REFERENCES consoles(id)

)
""")


connection.commit()

connection.close()


print("Sections table created!")