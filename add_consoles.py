import sqlite3


DATABASE = "archive.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


# Remove old console data
cursor.execute("""
DELETE FROM consoles
""")

# Reset ID counter
cursor.execute("""
DELETE FROM sqlite_sequence
WHERE name='consoles'
""")


consoles = [

    ("ps1", "PlayStation", "theme-ps1"),

    ("ps2", "PlayStation 2", "theme-ps2"),

    ("ps3", "PlayStation 3", "theme-ps3"),

    ("ps4", "PlayStation 4", "theme-ps4"),

    ("ps5", "PlayStation 5", "theme-ps5")

]


cursor.executemany("""
INSERT INTO consoles (slug, name, theme)
VALUES (?, ?, ?)
""", consoles)


connection.commit()

connection.close()


print("Consoles reset successfully!")