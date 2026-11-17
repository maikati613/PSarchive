from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


DATABASE = "archive.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


# =========================
# Main Pages
# =========================


@app.route("/")
def home():
    return render_template(
        "home.html",
        theme="theme-playstation",
        archive=False
    )


@app.route("/history")
def history():
    return render_template(
        "history.html",
        theme="theme-playstation",
        archive=False
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        theme="theme-playstation",
        archive=False
    )


@app.route("/legacy")
def legacy():
    return render_template(
        "legacy.html",
        theme="theme-playstation",
        archive=False
    )


@app.route("/exclusives")
def exclusives():
    return render_template(
        "exclusives.html",
        theme="theme-playstation",
        archive=False
    )



# =========================
# Database Archive System
# =========================


@app.route("/TheCompleteArchive/<console>")
def archive(console):

    connection = get_db_connection()


    selected_console = connection.execute("""
        SELECT *
        FROM consoles
        WHERE slug = ?
    """, (console,)).fetchone()


    if selected_console is None:
        connection.close()
        return "Console not found"


    sections = connection.execute("""
        SELECT *
        FROM sections
        WHERE console_id = ?
        ORDER BY display_order
    """, (selected_console["id"],)).fetchall()


    connection.close()


    return render_template(
        "TheCompleteArchive.html",
        console=selected_console,
        sections=sections,
        theme=selected_console["theme"],
        archive=True
    )



if __name__ == "__main__":
    app.run(debug=True)