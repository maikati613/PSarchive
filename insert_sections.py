import sqlite3

DATABASE = "archive.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


def get_console_id(slug):
    return cursor.execute(
        "SELECT id FROM consoles WHERE slug = ?",
        (slug,)
    ).fetchone()[0]


def add_section(slug, title, content, order):
    console_id = get_console_id(slug)

    cursor.execute("""
        INSERT INTO sections
        (console_id, title, content, display_order)
        VALUES (?, ?, ?, ?)
    """, (console_id, title, content, order))


# =========================
# PlayStation (PS1)
# =========================

add_section(
    "ps1",
    "Overview",
    """The original PlayStation was released by Sony Computer Entertainment
in Japan on December 3, 1994, and later launched worldwide in 1995.

It was Sony's first home video game console and marked the company's
entry into the gaming industry. The system became one of the most
important consoles in gaming history by popularizing 3D graphics,
CD-based games, and cinematic storytelling.""",
    1
)

add_section(
    "ps1",
    "Development and Release",
    """The PlayStation was originally created after a failed partnership
between Sony and Nintendo. Sony had been developing technology for a
CD-ROM add-on for the Super Nintendo Entertainment System, but the
project was cancelled.

Instead of abandoning the technology, Sony decided to create its own
console. The result was the PlayStation, designed around affordable
hardware and CD-ROM technology.

The console released with a focus on attracting both developers and
players, which helped it quickly gain popularity.""",
    2
)

add_section(
    "ps1",
    "Hardware Specifications",
    """CPU:
32-bit RISC processor running at 33.8688 MHz

Memory:
2 MB RAM

Graphics:
1 MB VRAM with dedicated 3D rendering capabilities

Storage:
CD-ROM format capable of storing much larger games than cartridges""",
    3
)

add_section(
    "ps1",
    "Impact on Gaming",
    """The PlayStation changed the video game industry by making 3D gaming
more accessible and encouraging developers to create larger,
more cinematic experiences.

The use of CDs allowed games to include higher quality audio,
voice acting, and longer stories.

The console also helped gaming become more accepted by older
audiences because of titles that focused on mature storytelling.""",
    4
)

add_section(
    "ps1",
    "Important Games",
    """• Final Fantasy VII

• Metal Gear Solid

• Gran Turismo

• Resident Evil

• Crash Bandicoot

• Tekken 3

• Spyro the Dragon""",
    5
)

add_section(
    "ps1",
    "Legacy",
    """The original PlayStation sold over 100 million units worldwide and
established PlayStation as one of the biggest names in gaming.

Its success created the foundation for future PlayStation consoles
and influenced how games were designed for decades.

The PS1 remains remembered as one of the most influential consoles
ever created.""",
    6
)


connection.commit()
connection.close()

print("PS1 sections added successfully!")