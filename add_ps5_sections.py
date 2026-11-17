import sqlite3


DATABASE = "archive.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


sections = [

    (
        5,
        "Overview",
        """
The PlayStation 5 was released by Sony Interactive Entertainment
on November 12, 2020, beginning the ninth generation of video game
consoles.

The PS5 was designed around faster loading speeds, advanced graphics,
immersive audio, and a new generation of gameplay experiences.

It introduced a custom solid-state drive, ray tracing technology,
the DualSense controller, and improved support for high-resolution
gaming.
""",
        1
    ),

    (
        5,
        "Development and Release",
        """
Sony began developing the PlayStation 5 with the goal of removing
limitations from previous generations.

One of the main focuses was reducing loading times. Traditional hard
drives had become a major limitation, so Sony created a custom SSD
architecture designed specifically for gaming.

The console launched in November 2020 during a period of extremely
high demand. Due to supply limitations, many players experienced
difficulty purchasing the system during its first years.
""",
        2
    ),

    (
        5,
        "Hardware Specifications",
        """
The PlayStation 5 introduced a major increase in performance compared
to the PlayStation 4.

CPU:

AMD Zen 2 8-core processor

GPU:

AMD RDNA 2-based graphics processor

Memory:

16 GB GDDR6 RAM

Storage:

Custom 825 GB SSD in the original model with expandable storage
support

Resolution:

Support for 4K gaming, high frame rates, and advanced visual features
""",
        3
    ),

    (
        5,
        "Custom SSD Technology",
        """
The PS5's custom SSD is one of its most important technological
features.

Compared to traditional hard drives, the SSD allows games to load
much faster and enables developers to create larger and more detailed
worlds.

The faster storage also allows game environments to be designed with
fewer loading interruptions, creating smoother experiences.
""",
        4
    ),

    (
        5,
        "DualSense Controller",
        """
The DualSense controller introduced new ways for players to interact
with games.

Its main features include:

• Adaptive triggers that can change resistance depending on gameplay

• Haptic feedback for more detailed vibrations and sensations

• Built-in microphone

• Improved motion controls

These features were designed to make gameplay feel more immersive
than previous PlayStation controllers.
""",
        5
    ),

    (
        5,
        "Ray Tracing and Graphics",
        """
The PlayStation 5 introduced advanced graphical features such as
hardware-based ray tracing.

Ray tracing allows games to simulate realistic lighting, reflections,
and shadows.

Combined with improved processing power, the PS5 allows developers
to create more detailed environments and more realistic visual
effects.
""",
        6
    ),

    (
        5,
        "Important Games",
        """
The PlayStation 5 has continued PlayStation's tradition of strong
exclusive and first-party experiences.

• Marvel's Spider-Man 2

• Horizon Forbidden West

• Demon's Souls Remake

• Ratchet & Clank: Rift Apart

• Returnal

• Gran Turismo 7

• Astro Bot

• God of War Ragnarök
""",
        7
    ),

    (
        5,
        "PS5 Slim and PS5 Pro",
        """
Sony released the PS5 Slim in 2023, introducing a smaller and lighter
design while maintaining similar performance.

In 2024, Sony released the PlayStation 5 Pro, an upgraded model
designed to provide improved graphics performance, enhanced ray
tracing, and higher quality visuals for compatible games.
""",
        8
    ),

    (
        5,
        "Legacy and Future",
        """
The PlayStation 5 continues the legacy created by previous PlayStation
generations.

It combines the storytelling focus of PlayStation consoles with
modern technology such as high-speed storage, advanced graphics,
and immersive controllers.

The PS5 represents Sony's current vision for the future of gaming,
building on more than three decades of PlayStation history.
""",
        9
    )

]


cursor.executemany("""
INSERT INTO sections
(console_id, title, content, display_order)
VALUES (?, ?, ?, ?)
""", sections)


connection.commit()

connection.close()


print("PS5 sections added successfully!")