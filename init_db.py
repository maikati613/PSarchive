import sqlite3

connection = sqlite3.connect("archive.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    console TEXT NOT NULL,
    release_year INTEGER,
    description TEXT,
    image TEXT
)
""")

connection.commit()
connection.close()

print("Database initialized successfully!")