import sqlite3


DATABASE = "archive.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


sections = [

    (
        3,
        "Overview",
        """
The PlayStation 3 was released by Sony Computer Entertainment
in Japan on November 11, 2006, and later launched worldwide.

The console introduced a new generation of gaming with high-definition
graphics, Blu-ray technology, online services through PlayStation
Network, and powerful hardware designed for advanced computing.

Although its launch was challenging due to its high price and complex
architecture, the PS3 eventually became known for its strong lineup
of exclusive games and important technological innovations.
""",
        1
    ),

    (
        3,
        "Development and Release",
        """
Sony designed the PlayStation 3 as a major technological step forward
from the PlayStation 2.

The console was built around the Cell Broadband Engine processor,
a powerful architecture created through a partnership between Sony,
IBM, and Toshiba.

The PS3 also introduced Blu-ray as its main game format, helping Sony
promote the new optical disc technology during the competition against
HD DVD.

The console launched at a high price because of its advanced hardware,
which made the beginning of its life cycle difficult.
""",
        2
    ),

    (
        3,
        "Hardware Specifications",
        """
The PlayStation 3 featured some of the most advanced hardware of its
generation.

CPU:

Cell Broadband Engine processor with one main Power Processing Element
and multiple Synergistic Processing Elements

GPU:

NVIDIA RSX Reality Synthesizer

Memory:

256 MB XDR RAM and 256 MB GDDR3 VRAM

Storage:

Blu-ray discs with built-in hard drive options
""",
        3
    ),

    (
        3,
        "Blu-ray and Technology",
        """
A major feature of the PlayStation 3 was its built-in Blu-ray player.

Sony used the console as a way to support Blu-ray during the format
competition against HD DVD.

The inclusion of Blu-ray allowed games to use much larger storage
capacity compared to DVDs, enabling developers to create more
detailed worlds, higher quality audio, and larger experiences.
""",
        4
    ),

    (
        3,
        "PlayStation Network",
        """
The PlayStation 3 expanded Sony's online gaming services through
PlayStation Network.

Players could access online multiplayer, digital purchases,
downloadable content, streaming services, and communication features.

The PS3 era helped establish many online features that would become
standard on future PlayStation consoles.
""",
        5
    ),

    (
        3,
        "Important Games",
        """
The PlayStation 3 became famous for its exclusive games and
story-driven experiences.

• The Last of Us

• Uncharted series

• Metal Gear Solid 4: Guns of the Patriots

• LittleBigPlanet

• Demon's Souls

• God of War III

• Gran Turismo 5

• Heavy Rain
""",
        6
    ),

    (
        3,
        "Recovery and Success",
        """
After its difficult launch, Sony improved the PS3 through price
reductions, redesigned models, and a stronger focus on exclusive
software.

Games such as The Last of Us and the Uncharted series helped improve
the console's reputation and demonstrated the power of first-party
PlayStation studios.
""",
        7
    ),

    (
        3,
        "Legacy",
        """
The PlayStation 3 sold over 87 million units worldwide and became an
important part of PlayStation history.

Although its early years were challenging, the console introduced
technologies that influenced future gaming, including Blu-ray,
digital distribution, online services, and advanced game development
techniques.

The PS3 is remembered as a console that evolved significantly during
its lifetime.
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


print("PS3 sections added successfully!")