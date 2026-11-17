import sqlite3


DATABASE = "archive.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


# =========================
# Consoles Table
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS consoles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    slug TEXT NOT NULL,

    name TEXT NOT NULL,

    theme TEXT NOT NULL

)
""")


# =========================
# Sections Table
# =========================

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


print("Database created successfully!")