import sqlite3

DATABASE = "archive.db"


def get_db_connection():

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    return connection


def add_sections():

    connection = get_db_connection()

    cursor = connection.cursor()

    # Delete all legacy sections before inserting new ones
    cursor.execute("""
        DELETE FROM sections
        WHERE console_id >= 6
    """)

    sections = [

        # PSP
        (
            6,
            "Overview",
            """
The PlayStation Portable (PSP) was released by Sony
Computer Entertainment in 2004 and was Sony's first
handheld gaming system.

The PSP brought the PlayStation experience into a
portable format, offering console-quality graphics,
a widescreen display, and multimedia features.

The system became one of Sony's most successful
hardware projects outside of its main consoles.
""",
            1
        ),


        (
            6,
            "Development and Release",
            """
Sony created the PSP to enter the handheld gaming market
and compete with Nintendo.

The goal was to create a portable system that could
deliver experiences closer to home consoles while also
supporting music, movies, and online features.

The PSP launched in 2004 and became one of Sony's most
successful hardware products.
""",
            2
        ),


        (
            6,
            "Hardware Specifications",
            """
CPU:

MIPS R4000-based processor running at 333 MHz


Display:

4.3 inch widescreen LCD display


Memory:

32 MB RAM


Storage:

Universal Media Disc (UMD)
and Memory Stick storage


Connectivity:

Wi-Fi and USB
""",
            3
        ),


        (
            6,
            "Important Games",
            """
The PSP received many important PlayStation titles.


• God of War: Chains of Olympus

• Metal Gear Solid: Peace Walker

• Crisis Core: Final Fantasy VII

• Gran Turismo PSP

• Monster Hunter Freedom

• Patapon
""",
            4
        ),


        (
            6,
            "Legacy",
            """
The PSP sold over 80 million units worldwide.

It proved that handheld systems could deliver
console-quality gaming experiences and became one of
Sony's most memorable hardware projects.

The PSP remains popular because of its unique design,
large library, and ambitious technology.
""",
            5
        )

    ]


    cursor.executemany(

        """
        INSERT INTO sections
        (
            console_id,
            title,
            content,
            display_order
        )

        VALUES
        (
            ?,
            ?,
            ?,
            ?
        )
        """,

        sections
    )


    connection.commit()

    connection.close()


    print("Legacy sections added successfully!")



if __name__ == "__main__":

    add_sections()