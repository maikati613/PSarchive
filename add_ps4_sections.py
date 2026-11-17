import sqlite3


DATABASE = "archive.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


sections = [

    (
        4,
        "Overview",
        """
The PlayStation 4 was released by Sony Computer Entertainment
on November 15, 2013, in North America, followed by releases in
other regions later that year.

The console focused on powerful but accessible hardware, improved
development tools, social features, and a strong connection between
players and games.

The PS4 became one of Sony's most successful consoles, selling over
117 million units worldwide and becoming a major platform for both
first-party and third-party developers.
""",
        1
    ),

    (
        4,
        "Development and Design",
        """
After learning from the challenges of the PlayStation 3 era, Sony
designed the PS4 with simplicity and accessibility in mind.

The console used a PC-like architecture based on AMD technology,
making it easier for developers to create games.

Sony focused on creating a developer-friendly system that allowed
studios to use the hardware efficiently while reducing development
complexity.
""",
        2
    ),

    (
        4,
        "Hardware Specifications",
        """
The PlayStation 4 introduced a large improvement in processing power
compared to previous generations.

CPU:

AMD Jaguar 8-core processor

GPU:

AMD Radeon-based graphics processor

Memory:

8 GB GDDR5 unified memory

Storage:

500 GB or 1 TB hard drive options

Resolution:

Support for Full HD gaming and later 4K enhancements through
PlayStation 4 Pro
""",
        3
    ),

    (
        4,
        "Social Features and Online Gaming",
        """
The PS4 introduced many features designed around sharing and
connecting players.

The DualShock 4 controller included a Share button that allowed users
to capture screenshots, record gameplay, and stream content.

PlayStation Network also expanded with digital purchases, online
multiplayer, and subscription services through PlayStation Plus.
""",
        4
    ),

    (
        4,
        "PlayStation 4 Pro",
        """
In 2016, Sony released the PlayStation 4 Pro, an upgraded version of
the console.

The PS4 Pro featured improved graphics performance, higher resolution
support, and better visual quality for compatible games.

It was designed for players using 4K televisions and helped introduce
the transition toward higher-resolution gaming.
""",
        5
    ),

    (
        4,
        "Important Games",
        """
The PlayStation 4 became known for its impressive collection of
exclusive games.

• Marvel's Spider-Man

• God of War (2018)

• Horizon Zero Dawn

• Ghost of Tsushima

• Bloodborne

• The Last of Us Part II

• Uncharted 4: A Thief's End

• Persona 5
""",
        6
    ),

    (
        4,
        "Impact on Gaming",
        """
The PS4 helped define modern gaming by focusing on digital
distribution, online communities, streaming, and large open-world
experiences.

Its architecture allowed developers to create detailed environments,
complex stories, and cinematic experiences.

The console also strengthened Sony's first-party studios, leading to
some of the most recognized games of the generation.
""",
        7
    ),

    (
        4,
        "Legacy",
        """
The PlayStation 4 is considered one of Sony's greatest successes.

With more than 117 million consoles sold worldwide, it became one of
the best-selling gaming systems ever created.

The PS4 established many features that continue into the PlayStation
5 generation, including digital gaming, online services, and a focus
on cinematic single-player experiences.
""",
        8
    )

]


cursor.executemany("""
INSERT INTO sections
(console_id, title, content, display_order)
VALUES (?, ?, ?, ?)
""", sections)


connection.commit()

connection.close()


print("PS4 sections added successfully!")