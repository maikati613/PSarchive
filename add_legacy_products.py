import sqlite3

DATABASE = "archive.db"


# ==================================================
# PLAYSTATION VITA SECTIONS
# console_id = 8
# ==================================================

sections = [

(
8,
"Overview",
"""
The PlayStation Vita was released by Sony Computer Entertainment
in 2011 as the successor to the PlayStation Portable.

Designed as a premium handheld gaming system, the Vita featured
console-quality graphics, dual analog sticks, touch controls,
and deep PlayStation Network integration.

Although it never reached the commercial success of the PSP,
the Vita became one of Sony's most technically advanced
portable systems.
""",
1
),

(
8,
"Development and Release",
"""
Sony developed the Vita to compete in the growing handheld
gaming market while expanding digital gaming.

The system launched in Japan in late 2011 and worldwide
during 2012.

It introduced many modern ideas including digital purchases,
cross-save functionality, and Remote Play.
""",
2
),

(
8,
"Hardware Specifications",
"""
CPU:

Quad-core ARM Cortex-A9 processor

GPU:

PowerVR SGX543MP4+

Display:

5 inch OLED display (original model)

Memory:

512 MB RAM

Storage:

PlayStation Vita Memory Cards

Connectivity:

Wi-Fi
Optional 3G on selected models
""",
3
),

(
8,
"Features",
"""
PlayStation Vita introduced:

• Dual analog sticks

• Front touchscreen

• Rear touch panel

• Front and rear cameras

• Motion controls

• PlayStation Network

• Remote Play

• Cross-Buy and Cross-Save support
""",
4
),

(
8,
"Important Games",
"""
Major PlayStation Vita games included:

• Uncharted: Golden Abyss

• Persona 4 Golden

• Gravity Rush

• Killzone Mercenary

• Tearaway

• Freedom Wars

• Soul Sacrifice
""",
5
),

(
8,
"Legacy",
"""
Although the Vita sold fewer units than Sony expected,
its hardware received widespread praise.

Today it maintains a passionate fan community and is
considered one of the finest handheld gaming systems
ever created.

Many players continue to appreciate its display,
controls, and unique library of games.
""",
6
)

]


# ==================================================
# DATABASE INSERT
# ==================================================

try:

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    added = 0

    for section in sections:

        cursor.execute(
            """
            INSERT INTO sections
            (console_id, title, content, display_order)
            VALUES (?, ?, ?, ?)
            """,
            section
        )

        added += 1


    conn.commit()
    conn.close()


    print("=================================")
    print("✅ SUCCESS!")
    print(f"Added {added} PlayStation Vita sections.")
    print("=================================")


except Exception as e:

    print("=================================")
    print("❌ ERROR:")
    print(e)
    print("=================================")