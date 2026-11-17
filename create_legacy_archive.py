import sqlite3


# ==========================================
# DATABASE SETTINGS
# ==========================================

DATABASE = "archive.db"



def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection



# ==========================================
# CREATE LEGACY TABLE
# ==========================================

def create_legacy_table():

    connection = get_db_connection()

    cursor = connection.cursor()


    cursor.execute("""

    CREATE TABLE IF NOT EXISTS legacy_items (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        category TEXT NOT NULL,

        release_year INTEGER,

        manufacturer TEXT,

        history TEXT,

        hardware TEXT,

        features TEXT,

        games TEXT,

        legacy TEXT,

        image TEXT

    )

    """)


    connection.commit()

    connection.close()



# ==========================================
# INSERT LEGACY PRODUCTS
# ==========================================

def insert_legacy_items():

    connection = get_db_connection()

    cursor = connection.cursor()



    # Prevent duplicate data

    cursor.execute("""

                   DELETE
                   FROM legacy_items

                   """)

    # Reset ID counter

    cursor.execute("""

                   DELETE
                   FROM sqlite_sequence

                   WHERE name = 'legacy_items'

                   """)



    legacy_items = [



# ==================================================
# PSP
# ==================================================

(
"PlayStation Portable (PSP)",

"Handheld Console",

2004,

"Sony Computer Entertainment",


"""
The PlayStation Portable, commonly known as the PSP,
was Sony's first handheld gaming system.

Released in 2004 in Japan and later worldwide,
the PSP was created to bring the PlayStation experience
into a portable format.

Sony wanted to challenge the dominance of Nintendo's
handheld systems by offering console-like graphics,
multimedia features, and a premium design.

The PSP became one of Sony's most successful hardware
projects outside of its main PlayStation consoles.
""",


"""
The PSP featured a 4.3 inch widescreen LCD display,
a custom MIPS processor, 32MB of RAM, Wi-Fi connectivity,
and removable Memory Stick storage.

One of its most unique features was the Universal Media Disc
(UMD), a small optical disc format created specifically
for the system.

The hardware was considered extremely powerful for a
handheld device when it launched.
""",


"""
The PSP was designed as more than just a gaming device.

It supported:

- Gaming
- Music playback
- Movies through UMD
- Photo viewing
- Internet browsing
- Digital downloads

Later models improved battery life, reduced size,
and introduced new designs such as the PSP Go.
""",


"""
The PSP received many important PlayStation franchises.

Major games included:

- God of War: Chains of Olympus
- Gran Turismo PSP
- Metal Gear Solid: Peace Walker
- Monster Hunter Freedom series
- Final Fantasy titles
- Crisis Core: Final Fantasy VII

The system also received many original games
and PlayStation classics through digital releases.
""",


"""
The PSP sold over 80 million units worldwide.

It proved that handheld systems could provide
console-quality gaming experiences and helped establish
Sony as a major competitor in the portable gaming market.

The PSP remains one of the most remembered PlayStation
devices because of its unique design, large library,
and multimedia abilities.
""",


"psp.jpg"

),



# ==================================================
# PSP GO
# ==================================================

(
"PlayStation Portable Go",

"Handheld Console",

2009,

"Sony Computer Entertainment",


"""
The PSP Go was a redesigned version of the original PSP.

Released in 2009, Sony created the PSP Go as a smaller,
fully digital handheld system.

Unlike previous PSP models, it removed the UMD drive
and focused entirely on downloadable games through
the PlayStation Store.
""",


"""
The PSP Go featured:

- A sliding screen design
- 3.8 inch display
- 16GB internal storage
- Bluetooth support
- Smaller body compared to previous PSP models

The removal of physical media allowed Sony to create
a much smaller device.
""",


"""
The PSP Go introduced a completely digital future
for PlayStation handheld gaming.

It supported:

- Digital PSP games
- Video downloads
- Music
- PlayStation Network features
- Remote Play with PlayStation 3
""",


"""
The PSP Go used the same software library as the PSP.

Compatible games included:

- Gran Turismo PSP
- God of War titles
- Metal Gear Solid: Peace Walker
- Final Fantasy games
""",


"""
Although the PSP Go was innovative,
it was criticized because of its higher price,
lack of physical games,
and limited storage options at launch.

Despite poor sales, it was an early example of
Sony experimenting with an all-digital gaming future.
""",


"pspgo.jpg"

),



# ==================================================
# PLAYSTATION VITA
# ==================================================

(
"PlayStation Vita",

"Handheld Console",

2011,

"Sony Computer Entertainment",


"""
The PlayStation Vita was Sony's successor to the PSP.

Released in 2011, the Vita was designed as a powerful
next-generation handheld system capable of delivering
console-like experiences.

Sony positioned the Vita as a premium portable device
with advanced controls and social features.
""",


"""
The Vita featured:

- 5 inch OLED touchscreen
- Rear touch panel
- Dual analog sticks
- Front and rear cameras
- Wi-Fi and optional 3G
- PlayStation Vita memory cards

The OLED model became known for its high quality display.
""",


"""
The Vita introduced many new features:

- Touch controls
- Remote Play with PlayStation 4
- PlayStation Network integration
- Digital game purchases
- Cross-platform features
""",


"""
Important Vita games included:

- Uncharted: Golden Abyss
- Gravity Rush
- Killzone Mercenary
- Persona 4 Golden
- Tearaway
- Freedom Wars
""",


"""
Although the Vita did not reach the success of the PSP,
it developed a passionate fanbase.

Its hardware was praised,
and it is remembered today as one of Sony's
most ambitious handheld projects.
""",


"vita.jpg"

),

# ==================================================
# PLAYSTATION TV
# ==================================================

    (
    "PlayStation TV",

    "Microconsole / Media Device",

    2013,

    "Sony Computer Entertainment",

    """
    PlayStation TV was a small entertainment device
    based on the hardware architecture of the PlayStation Vita.

    Originally released in Japan as PlayStation Vita TV,
    Sony designed the system as a way to bring Vita games,
    media applications, and Remote Play features to a television.

    The device represented Sony's attempt to create a small,
    affordable PlayStation ecosystem outside of its main consoles.
    """,

    """
    PlayStation TV contained hardware similar to the PlayStation Vita.

    It included:

    - ARM Cortex-A9 processor
    - PowerVR SGX543MP4+ graphics
    - 1GB RAM
    - HDMI output
    - USB connectivity
    - Memory card support

    Unlike the Vita handheld, it removed the built-in screen,
    controls, cameras, and battery.
    """,

    """
    The system supported:

    - PlayStation Vita games
    - PlayStation Network access
    - Remote Play with PlayStation 4
    - Video streaming applications
    - Digital downloads

    A DualShock controller was used instead of built-in handheld controls.
    """,

    """
    Compatible games included many PlayStation Vita titles,
    although not the entire Vita library.

    The system also allowed players to stream
    PlayStation 4 games to another television through Remote Play.
    """,

    """
    PlayStation TV was an interesting idea that arrived before
    streaming and remote gaming became mainstream.

    However, limited game compatibility,
    confusing marketing, and competition from other streaming devices
    caused weak sales.

    Today it is remembered as an unusual and experimental
    piece of PlayStation hardware.
    """,

    "pstv.jpg"

),

        # ==================================================
        # PLAYSTATION VR
        # ==================================================

        (
            "PlayStation VR",

            "Virtual Reality Headset",

            2016,

            "Sony Interactive Entertainment",

            """
            PlayStation VR was Sony's first major entry into
            virtual reality gaming.
        
            Released for PlayStation 4 in 2016,
            it allowed console players to experience VR without
            requiring an expensive gaming PC.
        
            Sony aimed to make virtual reality more accessible
            to a wider audience.
            """,

            """
            The headset featured:
        
            - 5.7 inch OLED display
            - 1920xRGBx1080 resolution
            - 120Hz refresh rate
            - Integrated tracking lights
            - 360 degree head tracking
        
            The system used the PlayStation Camera
            and PlayStation Move controllers for tracking.
            """,

            """
            PlayStation VR introduced:
        
            - Immersive virtual reality gaming
            - 3D audio experiences
            - Motion-based controls
            - Cinematic Mode for normal PS4 games
        
            It allowed players to experience games
            from inside virtual worlds.
            """,

            """
            Important PlayStation VR games included:
        
            - Astro Bot Rescue Mission
            - Resident Evil 7 VR
            - Blood & Truth
            - Beat Saber
            - Iron Man VR
            - Skyrim VR
            """,

            """
            PlayStation VR became one of the most successful
            consumer VR headsets of its generation.
        
            It helped prove that virtual reality could exist
            on a traditional home console and created a foundation
            for Sony's future VR technology.
            """,

            "psvr.jpg"

        ),

        # ==================================================
        # PLAYSTATION VR2
        # ==================================================

        (
            "PlayStation VR2",

            "Virtual Reality Headset",

            2023,

            "Sony Interactive Entertainment",

            """
            PlayStation VR2 is Sony's second-generation
            virtual reality headset.
        
            Designed exclusively for PlayStation 5,
            it was created to improve upon the original PS VR
            with modern hardware and deeper immersion.
        
            Sony focused on higher quality visuals,
            better tracking, and stronger interaction.
            """,

            """
            PlayStation VR2 features:
        
            - OLED HDR displays
            - 2000x2040 resolution per eye
            - Eye tracking
            - Inside-out tracking cameras
            - Sense controllers
            - Headset vibration
        
            Unlike the original PS VR,
            it does not require an external camera.
            """,

            """
            New features include:
        
            - Eye tracking
            - Foveated rendering
            - Adaptive triggers
            - Advanced haptic feedback
            - Finger touch detection
        
            These features allow games to react
            more naturally to player movement.
            """,

            """
            Major games include:
        
            - Horizon Call of the Mountain
            - Gran Turismo 7 VR
            - Resident Evil Village VR
            - Resident Evil 4 VR Mode
            - No Man's Sky VR
            """,

            """
            PlayStation VR2 represents Sony's continued investment
            in virtual reality.
        
            Although the VR market remains smaller than traditional gaming,
            PS VR2 demonstrates PlayStation's commitment to immersive
            gaming experiences.
            """,

            "psvr2.jpg"

        ),

        # ==================================================
        # PLAYSTATION PORTAL
        # ==================================================

        (
            "PlayStation Portal",

            "Remote Play Device",

            2023,

            "Sony Interactive Entertainment",

            """
            PlayStation Portal is a handheld remote-play device
            created for PlayStation 5.
        
            Unlike traditional handheld consoles,
            Portal does not run games independently.
            Instead, it streams games directly from a player's PS5.
        
            Sony designed it for players who want to use their PS5
            away from the main television.
            """,

            """
            PlayStation Portal features:
        
            - 8 inch LCD display
            - DualSense controller design
            - Adaptive triggers
            - Haptic feedback
            - Wi-Fi streaming technology
        
            The device combines a screen with
            the full DualSense control experience.
            """,

            """
            Features include:
        
            - PS5 Remote Play
            - DualSense functionality
            - Touchscreen controls
            - Console-quality controls anywhere in the home
        
            It focuses entirely on the PlayStation 5 ecosystem.
            """,

            """
            PlayStation Portal does not have exclusive games.
        
            Instead, it allows players to access
            their existing PS5 library remotely.
            """,

            """
            Portal represents a modern direction for PlayStation,
            where gaming experiences are expanded beyond
            the traditional television setup.
        
            It continues Sony's experiments with portable
            PlayStation experiences.
            """,

            "portal.jpg"

        ),

        # ==================================================
        # POCKETSTATION
        # ==================================================

        (
            "PocketStation",

            "Memory Card Accessory",

            1999,

            "Sony Computer Entertainment",

            """
            PocketStation was a unique accessory released
            for the original PlayStation.
        
            It combined a memory card with a miniature handheld device,
            allowing players to download small applications,
            mini-games, and additional content from compatible games.
            """,

            """
            PocketStation included:
        
            - Small LCD screen
            - Directional buttons
            - Infrared communication
            - Built-in memory
        
            It connected directly to the PlayStation
            through the memory card slot.
            """,

            """
            Features included:
        
            - Mini-games
            - Additional game content
            - Portable data storage
            - Communication between PocketStation devices
        
            It was one of Sony's earliest attempts
            at connecting console and portable gaming.
            """,

            """
            Compatible games included:
        
            - Final Fantasy VIII
            - Chocobo World
            - Street Fighter Alpha 3
            - Pocket MuuMuu
            """,

            """
            Although PocketStation never released worldwide,
            it became a memorable example of Sony experimenting
            with connected gaming experiences.
        
            Many of its ideas would later appear in
            future handheld and online features.
            """,

            "pocketstation.jpg"

),


# ==================================================
# PLAYSTATION CLASSIC
# ==================================================

(
"PlayStation Classic",

"Mini Console / Retro Hardware",

2018,

"Sony Interactive Entertainment",


"""
The PlayStation Classic was Sony's official miniature
recreation of the original PlayStation console.

Released in 2018 to celebrate the legacy of the first
PlayStation system, the device was designed as a nostalgic
product for fans who wanted to experience classic
PlayStation games on modern televisions.

The console recreated the iconic grey PlayStation design
in a much smaller form factor and represented Sony's attempt
to enter the growing retro gaming market.
""",


"""
The PlayStation Classic was approximately 45% smaller
than the original PlayStation.

Its hardware included:

- ARM-based processor
- HDMI output
- USB power connection
- Internal storage containing pre-installed games
- Two wired replica PlayStation controllers

Unlike the original PlayStation, it did not include
a disc drive and could not play physical discs.
""",


"""
The system included several modern features:

- HDMI support for modern televisions
- Save states
- Digital versions of classic PlayStation games
- Replica original PlayStation controller design

The controllers recreated the original PlayStation
gamepad but did not include analog sticks or vibration,
which limited compatibility with some later PS1 titles.
""",


"""
The PlayStation Classic included 20 built-in games.

Some included titles were:

- Final Fantasy VII
- Metal Gear Solid
- Tekken 3
- Ridge Racer Type 4
- Resident Evil Director's Cut
- Jumping Flash!

The selection differed between regions,
with some games being replaced depending on location.
""",


"""
The PlayStation Classic received mixed reactions.

While fans appreciated the nostalgic design,
many criticized the game selection,
lack of analog controllers,
and software emulation quality.

Despite its poor commercial reception,
the PlayStation Classic remains an interesting part
of PlayStation history because it represents Sony
revisiting and preserving its original console legacy.
""",


"ps_classic.jpg"

),
        # ==================================================
        # EYETOY
        # ==================================================

        (
            "EyeToy",

            "Camera Accessory",

            2003,

            "Sony Computer Entertainment",

            """
            EyeToy was a USB camera accessory released for the
            PlayStation 2 in 2003.
        
            It allowed players to interact with games using their
            body movements instead of a traditional controller.
        
            The device was one of Sony's earliest attempts at
            motion-based gaming and introduced millions of players
            to camera-controlled gameplay before motion controls
            became common in the industry.
            """,

            """
            The EyeToy camera featured:
        
            - USB connection
            - Built-in microphone
            - Video capture capabilities
            - Real-time player tracking
        
            The camera connected directly to the PlayStation 2
            and displayed the player's image on the television.
            """,

            """
            EyeToy introduced a new style of gameplay:
        
            - Motion-controlled interaction
            - Body movement recognition
            - Camera-based mini-games
            - Social party experiences
        
            Players could physically move in front of the camera
            to control games and activities.
            """,

            """
            Popular EyeToy games included:
        
            - EyeToy: Play
            - EyeToy: Groove
            - EyeToy: Kinetic
            - Sega Superstars
        
            The accessory received a large collection of
            family-friendly and experimental titles.
            """,

            """
            EyeToy was an important experiment in PlayStation history.
        
            Although it was eventually replaced by newer camera
            and motion technologies, it helped establish Sony's
            interest in interactive gaming beyond traditional
            controllers.
            """,

            "eyetoy.jpg"

        ),

        # ==================================================
        # PLAYSTATION EYE
        # ==================================================

        (
            "PlayStation Eye",

            "Camera Accessory",

            2007,

            "Sony Computer Entertainment",

            """
            The PlayStation Eye was the successor to EyeToy and
            was created for the PlayStation 3.
        
            Released in 2007, it improved camera technology,
            image quality, and microphone capabilities.
        
            The device became an important part of Sony's
            future motion-control plans.
            """,

            """
            The PlayStation Eye featured:
        
            - Higher resolution camera compared to EyeToy
            - Improved frame rate
            - Four microphone array
            - Better motion tracking
        
            It connected through USB and was designed
            specifically for PlayStation 3.
            """,

            """
            The camera supported:
        
            - Video chatting
            - Voice communication
            - Motion tracking
            - Augmented reality experiences
            - PlayStation Move tracking
        
            It became the foundation for Sony's later
            motion controller system.
            """,

            """
            Games and applications using PlayStation Eye included:
        
            - EyePet
            - The Eye of Judgment
            - PlayStation Move games
            - Various PlayStation Network applications
            """,

            """
            The PlayStation Eye was an important stepping stone
            between EyeToy and modern PlayStation VR technology.
        
            Its camera tracking technology helped Sony develop
            new ways for players to interact with games.
            """,

            "ps_eye.jpg"

        ),

        # ==================================================
        # PLAYSTATION MOVE
        # ==================================================

        (
            "PlayStation Move",

            "Motion Controller",

            2010,

            "Sony Computer Entertainment",

            """
            PlayStation Move was Sony's motion-control system
            released for PlayStation 3 in 2010.
        
            Created during the rise of motion gaming,
            Sony designed Move as a more precise alternative
            to traditional motion controllers.
        
            It used the PlayStation Eye camera to track
            the glowing controller sphere.
            """,

            """
            The PlayStation Move controller featured:
        
            - Motion sensors
            - Gyroscope
            - Accelerometer
            - Vibration feedback
            - Colored tracking sphere
            - Trigger button
        
            The system required the PlayStation Eye camera
            to accurately track movement.
            """,

            """
            PlayStation Move allowed players to:
        
            - Control games through physical movement
            - Use motion-based aiming
            - Interact with virtual objects
            - Play sports and party games
        
            It was later reused as a controller option
            for the original PlayStation VR headset.
            """,

            """
            Important PlayStation Move games included:
        
            - Sports Champions
            - Sorcery
            - Killzone 3
            - LittleBigPlanet 2
            - Until Dawn: Rush of Blood
            - Beat Saber (PS VR)
            """,

            """
            Although PlayStation Move never became as popular
            as Nintendo's Wii controls, it became an important
            part of Sony's experimentation with motion gaming.
        
            Its technology also helped form the foundation
            for PlayStation VR experiences.
            """,

            "move.jpg"

        ),

        # ==================================================
        # GOLD WIRELESS HEADSET
        # ==================================================

        (
            "Gold Wireless Headset",

            "Audio Accessory",

            2014,

            "Sony Computer Entertainment",

            """
            The Gold Wireless Headset was an official PlayStation
            audio accessory released for PlayStation 3 and later
            compatible with PlayStation 4.
        
            It was designed to provide players with a premium
            wireless audio experience while integrating directly
            with the PlayStation ecosystem.
        
            The headset became one of Sony's most popular official
            audio products during the PS4 generation.
            """,

            """
            The Gold Wireless Headset featured:
        
            - Wireless USB adapter
            - Virtual surround sound
            - Built-in microphone
            - Foldable design
            - Customizable audio profiles
        
            It was designed specifically for gaming rather than
            general music listening.
            """,

            """
            The headset supported:
        
            - Game audio
            - Voice chat
            - PlayStation Network communication
            - Custom sound modes through software
        
            Players could adjust audio settings through
            PlayStation applications.
            """,

            """
            The Gold Wireless Headset was compatible with many
            PlayStation games and became a common accessory
            for PS4 players.
        
            It was especially popular among players who wanted
            official PlayStation hardware without purchasing
            third-party gaming headsets.
            """,

            """
            The Gold Wireless Headset helped establish Sony's
            focus on official gaming audio products.
        
            It became a predecessor to later PlayStation headsets
            including the Platinum Wireless Headset and Pulse series.
            """,

            "gold_headset.jpg"

        ),

        # ==================================================
        # PLATINUM WIRELESS HEADSET
        # ==================================================

        (
            "Platinum Wireless Headset",

            "Audio Accessory",

            2017,

            "Sony Interactive Entertainment",

            """
            The Platinum Wireless Headset was Sony's premium
            official headset released during the PlayStation 4 era.
        
            It improved upon the Gold Wireless Headset by adding
            higher quality audio technology and more advanced
            features.
            """,

            """
            The Platinum Wireless Headset featured:
        
            - 50mm drivers
            - Wireless USB adapter
            - Built-in microphones
            - 3D audio support
            - Premium metal design
        
            It was created as a high-end alternative
            for PlayStation players.
            """,

            """
            Features included:
        
            - Virtual surround sound
            - Custom audio profiles
            - 3D audio support in compatible games
            - Voice chat support
        
            It was one of the first PlayStation accessories
            to introduce more advanced spatial audio features.
            """,

            """
            The headset was supported by many PS4 games
            with specially designed audio profiles.
        
            It was often used for competitive games where
            accurate sound positioning was important.
            """,

            """
            The Platinum Wireless Headset represented Sony's move
            toward more advanced gaming audio.
        
            Many of its ideas continued into the later
            Pulse 3D headset designed for PlayStation 5.
            """,

            "platinum_headset.jpg"

        ),

        # ==================================================
        # PULSE 3D WIRELESS HEADSET
        # ==================================================

        (
            "Pulse 3D Wireless Headset",

            "Audio Accessory",

            2020,

            "Sony Interactive Entertainment",

            """
            The Pulse 3D Wireless Headset was released alongside
            the PlayStation 5 in 2020.
        
            It was designed specifically to showcase Sony's
            Tempest 3D AudioTech, a new audio system created
            for the PS5 generation.
            """,

            """
            The headset featured:
        
            - Wireless USB adapter
            - Built-in microphones
            - 40mm drivers
            - USB-C charging
            - Dual noise-cancelling microphones
        
            Its design matched the futuristic appearance
            of the PlayStation 5 console.
            """,

            """
            The Pulse 3D headset supported:
        
            - Tempest 3D AudioTech
            - Game audio
            - Voice chat
            - Wireless PlayStation connectivity
            - PC compatibility
        
            It was created to provide immersive audio
            without requiring expensive equipment.
            """,

            """
            The headset was designed for PS5 launch titles
            and later supported many PlayStation games.
        
            It became the standard official headset
            for the early PS5 generation.
            """,

            """
            Pulse 3D became one of Sony's most recognizable
            PlayStation 5 accessories.
        
            It represented the next stage of PlayStation audio
            following the Gold and Platinum headset generations.
            """,

            "pulse3d.jpg"

        ),

        # ==================================================
        # PULSE ELITE
        # ==================================================

        (
            "Pulse Elite Wireless Headset",

            "Audio Accessory",

            2024,

            "Sony Interactive Entertainment",

            """
            Pulse Elite is Sony's premium wireless gaming headset
            for the PlayStation 5 generation.
        
            Released as part of Sony's new Pulse audio lineup,
            it was designed to provide higher-quality sound
            than the standard Pulse 3D headset.
            """,

            """
            Pulse Elite features:
        
            - Planar magnetic drivers
            - Retractable microphone
            - Wireless PlayStation Link technology
            - Charging hanger
            - Lossless audio support
        
            It uses technology normally found in
            higher-end audio equipment.
            """,

            """
            Features include:
        
            - Low latency wireless audio
            - PlayStation Link compatibility
            - PC compatibility
            - Bluetooth support
            - Advanced microphone controls
            """,

            """
            The Pulse Elite does not contain exclusive games,
            but it is designed to enhance the audio experience
            of the PlayStation 5 game library.
            """,

            """
            Pulse Elite represents Sony's move toward premium
            gaming audio and continues the evolution of
            official PlayStation headsets.
            """,

            "pulse_elite.jpg"

        ),

        # ==================================================
        # PULSE EXPLORE
        # ==================================================

        (
            "Pulse Explore Wireless Earbuds",

            "Audio Accessory",

            2023,

            "Sony Interactive Entertainment",

            """
            Pulse Explore are Sony's first official wireless
            gaming earbuds designed for the PlayStation ecosystem.
        
            Released alongside PlayStation Link technology,
            they provide a portable audio option for PlayStation
            players.
            """,

            """
            Pulse Explore features:
        
            - Planar magnetic drivers
            - Wireless PlayStation Link connection
            - Bluetooth support
            - Built-in microphones
            - Charging case
        
            They are designed for both gaming and mobile use.
            """,

            """
            Features include:
        
            - Low latency audio
            - PS5 compatibility
            - PlayStation Portal support
            - Mobile device connectivity
            - Voice communication
            """,

            """
            Pulse Explore earbuds work with:
        
            - PlayStation 5
            - PlayStation Portal
            - Compatible mobile devices
        
            They provide a portable alternative to traditional
            gaming headsets.
            """,

            """
            Pulse Explore expanded PlayStation's audio ecosystem
            beyond traditional headsets.
        
            They represent Sony's attempt to create a complete
            wireless audio platform around PlayStation devices.
            """,

            "pulse_explore.jpg"

        ),

        # ==================================================
        # DUALSENSE EDGE
        # ==================================================

        (
            "DualSense Edge",

            "Premium Controller",

            2023,

            "Sony Interactive Entertainment",

            """
            The DualSense Edge is Sony's premium professional
            controller designed for the PlayStation 5.
        
            Released in 2023, it was created for players who wanted
            more customization and advanced controls compared to
            the standard DualSense controller.
        
            It is PlayStation's first official high-performance
            controller similar to professional controllers
            from competitors.
            """,

            """
            The DualSense Edge features:
        
            - Replaceable analog stick modules
            - Adjustable triggers
            - Back buttons
            - Custom control profiles
            - Braided USB-C cable
            - Haptic feedback
            - Adaptive triggers
        
            The controller keeps the main design of the
            standard DualSense while adding professional features.
            """,

            """
            Features include:
        
            - Remappable buttons
            - Adjustable stick sensitivity
            - Multiple saved profiles
            - Quick profile switching
            - Swappable stick caps
            - Enhanced customization options
            """,

            """
            The DualSense Edge works with PlayStation 5 games
            and provides the same features as the normal DualSense:
        
            - Haptic feedback
            - Adaptive triggers
            - Motion controls
            - Touchpad support
            """,

            """
            The DualSense Edge represents Sony's move into
            the competitive gaming controller market.
        
            It gives advanced players more control while showing
            the continued evolution of PlayStation controllers.
            """,

            "dualsense_edge.jpg"

        ),

        # ==================================================
        # PLAYSTATION ACCESS CONTROLLER
        # ==================================================

        (
            "PlayStation Access Controller",

            "Accessibility Controller",

            2023,

            "Sony Interactive Entertainment",

            """
            The PlayStation Access Controller is an accessibility
            focused controller designed for PlayStation 5.
        
            Released in 2023, it was created to allow players
            with disabilities to customize their controls and
            create more comfortable gaming setups.
        
            It represents Sony's efforts toward making gaming
            more accessible.
            """,

            """
            The Access Controller features:
        
            - Large customizable buttons
            - Replaceable components
            - Multiple control layouts
            - Expansion port support
            - Adjustable button placement
        
            The design allows players to build a controller
            setup that fits their individual needs.
            """,

            """
            Features include:
        
            - Button remapping
            - Custom profiles
            - Compatibility with other accessibility devices
            - Flexible mounting options
            - Personalised control arrangements
            """,

            """
            The Access Controller supports PlayStation 5 games
            and works together with other accessibility devices
            to provide more options for players.
            """,

            """
            The Access Controller is an important milestone
            in PlayStation hardware history.
        
            It shows Sony expanding its hardware philosophy
            beyond performance and entertainment into
            greater accessibility.
            """,

            "access_controller.jpg"

        ),

        # ==================================================
        # BACK BUTTON ATTACHMENT
        # ==================================================

        (
            "Back Button Attachment",

            "Controller Accessory",

            2020,

            "Sony Interactive Entertainment",

            """
            The Back Button Attachment was an accessory released
            for the PlayStation 4 DualShock 4 controller.
        
            It added two programmable buttons on the back of the
            controller, allowing players to access commands without
            removing their thumbs from the analog sticks.
            """,

            """
            The accessory featured:
        
            - Two rear programmable buttons
            - OLED display
            - Easy connection to DualShock 4
            - Custom button mapping
        
            It attached directly to the controller's headset port.
            """,

            """
            Features included:
        
            - Button assignment customization
            - Faster access to important controls
            - Support for competitive gaming
        
            It was designed especially for players who wanted
            more advanced controller layouts.
            """,

            """
            The Back Button Attachment worked with the entire
            PlayStation 4 game library because it simply added
            extra controller inputs.
            """,

            """
            The accessory became popular among competitive players
            because it added features normally found in expensive
            custom controllers at a lower price.
            """,

            "back_button.jpg"

        ),

        # ==================================================
        # PLAYSTATION MEMORY CARD
        # ==================================================

        (
            "PlayStation Memory Card",

            "Storage Accessory",

            1994,

            "Sony Computer Entertainment",

            """
            The PlayStation Memory Card was the official storage
            accessory for the original PlayStation.
        
            Because the console did not contain internal storage,
            players used memory cards to save their game progress.
        
            It became one of the most recognizable accessories
            from the original PlayStation era.
            """,

            """
            The original PlayStation Memory Card featured:
        
            - 128KB storage capacity
            - Flash memory technology
            - PlayStation console compatibility
            - Compact design
        
            It connected through the controller ports
            on the front of the console.
            """,

            """
            The memory card allowed players to:
        
            - Save game progress
            - Store game settings
            - Transfer saves between consoles
        
            Players often owned multiple cards because storage
            space was limited.
            """,

            """
            Many PlayStation games required memory cards,
            including:
        
            - Final Fantasy VII
            - Metal Gear Solid
            - Resident Evil
            - Gran Turismo
            - Crash Bandicoot
            """,

            """
            The PlayStation Memory Card became an iconic part
            of the original PlayStation experience.
        
            Although simple by modern standards, it changed how
            players stored and managed their game progress.
            """,

            "memory_card.jpg"

        ),

        # ==================================================
        # PLAYSTATION MOUSE
        # ==================================================

        (
            "PlayStation Mouse",

            "Input Device",

            1994,

            "Sony Computer Entertainment",

            """
            The PlayStation Mouse was an official accessory
            released for the original PlayStation.
        
            Designed mainly for certain strategy, adventure,
            and creative games, it brought computer-style controls
            to the console.
            """,

            """
            The PlayStation Mouse featured:
        
            - Two-button design
            - Optical movement tracking
            - Connection through controller port
            - Compatible mouse pad
        
            It was designed similarly to a traditional computer mouse.
            """,

            """
            The accessory allowed:
        
            - Point-and-click controls
            - Menu navigation
            - More precise movement
            - Support for creative software
            """,

            """
            Compatible titles included:
        
            - Mario-style educational software
            - Adventure games
            - Strategy titles
            - Creative applications
        
            It was never a mainstream accessory but supported
            a unique group of PlayStation experiences.
            """,

            """
            The PlayStation Mouse represents Sony's early
            experimentation with different input methods.
        
            It showed that PlayStation was not limited to
            traditional console controls.
            """,

            "ps_mouse.jpg"

        ),

        # ==================================================
        # PSX
        # ==================================================

        (
            "PSX",

            "Entertainment System / DVR",

            2003,

            "Sony Computer Entertainment",

            """
            The PSX was a unique PlayStation device released only
            in Japan in 2003.
        
            Despite its name, the PSX was not the original
            PlayStation. Instead, it was a hybrid device based
            on PlayStation 2 hardware combined with digital
            video recording and home entertainment features.
        
            Sony designed it as an all-in-one entertainment machine.
            """,

            """
            The PSX featured:
        
            - PlayStation 2 hardware
            - Built-in hard drive
            - DVD recorder
            - TV tuner
            - Broadband connectivity
            - Digital media features
        
            It combined gaming with television recording
            and multimedia functions.
            """,

            """
            The PSX supported:
        
            - PlayStation 2 games
            - DVD playback
            - TV recording
            - Digital photo storage
            - Music playback
        
            It was designed to be the centre of a home
            entertainment setup.
            """,

            """
            Because the PSX was only released in Japan,
            its game compatibility was the same as the
            PlayStation 2 library.
        
            It was not a separate gaming platform.
            """,

            """
            The PSX is remembered as one of Sony's strangest
            PlayStation products.
        
            Although it was innovative, its high price and
            limited release prevented it from becoming successful.
        
            It remains an interesting example of Sony experimenting
            with the future of home entertainment.
            """,

            "psx.jpg"

        ),

        # ==================================================
        # PLAYSTATION 2 MULTITAP
        # ==================================================

        (
            "PlayStation 2 Multitap",

            "Controller Accessory",

            2000,

            "Sony Computer Entertainment",

            """
            The PlayStation 2 Multitap was an accessory that allowed
            multiple controllers and memory cards to connect to
            the PlayStation 2.
        
            It was created for multiplayer games that supported
            more than the console's standard two controllers.
            """,

            """
            The PlayStation 2 Multitap featured:
        
            - Four controller ports
            - Two memory card slots
            - Connection through controller port
        
            Using two Multitaps allowed up to eight players
            on supported games.
            """,

            """
            The accessory enabled:
        
            - Local multiplayer gaming
            - Large party games
            - Tournament-style gameplay
        
            It expanded the PlayStation 2's multiplayer capabilities.
            """,

            """
            Games supporting Multitap included:
        
            - Gran Turismo series
            - Pro Evolution Soccer
            - Bomberman
            - Multiplayer sports games
            """,

            """
            The PlayStation 2 Multitap became an important accessory
            during an era when local multiplayer gaming was a major
            part of console gaming culture.
            """,

            "ps2_multitap.jpg"

        ),

        # ==================================================
        # PLAYSTATION 3D DISPLAY
        # ==================================================

        (
            "PlayStation 3D Display",

            "Gaming Monitor",

            2011,

            "Sony Computer Entertainment",

            """
            The PlayStation 3D Display was an official Sony monitor
            released during the PlayStation 3 era.
        
            It was designed to showcase Sony's push toward
            3D gaming and stereoscopic entertainment.
            """,

            """
            The display featured:
        
            - 24 inch screen
            - Full HD resolution
            - Stereoscopic 3D support
            - HDMI connectivity
            - 3D glasses compatibility
        
            It was created specifically with PlayStation gaming
            in mind.
            """,

            """
            Features included:
        
            - 3D gaming support
            - Simultaneous two-player view mode
            - Built-in speakers
            - PlayStation branding and design
            """,

            """
            Compatible 3D games included:
        
            - Gran Turismo 5
            - Killzone 3
            - MotorStorm Apocalypse
            - Super Stardust HD
            """,

            """
            The PlayStation 3D Display represents Sony's attempt
            to bring 3D technology into mainstream gaming.
        
            Although 3D gaming eventually declined,
            it remains an interesting part of PS3 history.
            """,

            "ps3_display.jpg"

        ),

        # ==================================================
        # PLAYSTATION CAMERA PS4
        # ==================================================

        (
            "PlayStation Camera",

            "Camera Accessory",

            2013,

            "Sony Computer Entertainment",

            """
            The PlayStation Camera was released alongside the
            PlayStation 4.
        
            It continued Sony's experiments with camera-based
            interaction and later became an important accessory
            for PlayStation VR.
            """,

            """
            The PlayStation Camera featured:
        
            - Dual camera lenses
            - 3D depth sensing
            - Built-in microphone array
            - Motion tracking
            - Voice recognition
        
            It connected directly to the PlayStation 4.
            """,

            """
            The camera supported:
        
            - PlayStation VR tracking
            - Broadcasting gameplay
            - Voice commands
            - Facial recognition
            - Motion-based games
            """,

            """
            The PlayStation Camera was used by several games
            and became essential for the original PlayStation VR
            system.
            """,

            """
            The camera continued Sony's long history of exploring
            alternative ways to interact with games, following
            EyeToy and PlayStation Eye.
            """,

            "ps_camera.jpg"

        ),

        # ==================================================
        # PLAYSTATION VITA MEMORY CARD
        # ==================================================

        (
            "PlayStation Vita Memory Card",

            "Storage Accessory",

            2011,

            "Sony Computer Entertainment",

            """
            The PlayStation Vita Memory Card was Sony's proprietary
            storage format created specifically for the PlayStation Vita.
        
            Unlike standard SD cards, Vita memory cards were designed
            to work only with Sony's handheld system.
            """,

            """
            The memory cards were available in multiple sizes:
        
            - 4GB
            - 8GB
            - 16GB
            - 32GB
            - 64GB
        
            They were required for many digital games
            and applications.
            """,

            """
            The cards allowed players to store:
        
            - Digital games
            - Save files
            - Downloaded content
            - Applications
            - Media files
            """,

            """
            The proprietary design became controversial because
            of high prices compared to standard memory cards.
            """,

            """
            The Vita Memory Card became a defining part of the
            PlayStation Vita experience and influenced discussions
            about proprietary storage.
            """,

            "vita_memory.jpg"

        ),

        # ==================================================
        # PLAYSTATION VR AIM CONTROLLER
        # ==================================================

        (
            "PlayStation VR Aim Controller",

            "VR Motion Controller",

            2017,

            "Sony Interactive Entertainment",

            """
            The PlayStation VR Aim Controller was a specialized
            controller created for PlayStation VR shooters.
        
            It was designed to provide a more realistic way
            to interact with virtual weapons.
            """,

            """
            The controller featured:
        
            - Motion tracking sphere
            - Analog sticks
            - Trigger buttons
            - Motion sensors
            - Vibration feedback
        
            It combined traditional controls with VR movement.
            """,

            """
            The controller allowed:
        
            - Realistic aiming
            - Weapon handling
            - Two-handed VR interactions
            - Immersive shooting experiences
            """,

            """
            Games using the VR Aim Controller included:
        
            - Farpoint
            - Firewall Zero Hour
            - Arizona Sunshine
            """,

            """
            The VR Aim Controller showed Sony's effort to create
            specialized hardware for different VR experiences.
        
            It remains one of the most unique PlayStation VR accessories.
            """,

            "vr_aim.jpg"

        ),

        # ==================================================
        # PLAYSTATION MOVE NAVIGATION CONTROLLER
        # ==================================================

        (
            "PlayStation Move Navigation Controller",

            "Motion Controller Accessory",

            2010,

            "Sony Computer Entertainment",

            """
            The PlayStation Move Navigation Controller was a
            secondary controller designed to be used alongside
            the PlayStation Move controller.
        
            It provided additional buttons and analog movement
            for more complex motion games.
            """,

            """
            The controller featured:
        
            - Analog stick
            - Directional buttons
            - Trigger button
            - Shoulder buttons
            - Motion tracking compatibility
            """,

            """
            It was designed to provide:
        
            - Movement control
            - More traditional navigation
            - Better gameplay comfort in motion titles
            """,

            """
            The Navigation Controller was used in various
            PlayStation Move games but was eventually replaced
            by newer control methods.
            """,

            """
            The controller represents Sony's attempt to combine
            traditional game controls with motion gaming.
            """,

            "move_navigation.jpg"

        ),
]



    cursor.executemany("""

    INSERT INTO legacy_items

    (

    name,
    category,
    release_year,
    manufacturer,
    history,
    hardware,
    features,
    games,
    legacy,
    image

    )

    VALUES

    (?,?,?,?,?,?,?,?,?,?)

    """, legacy_items)



    connection.commit()

    connection.close()



# ==========================================
# RUN SCRIPT
# ==========================================

if __name__ == "__main__":

    print("Creating PlayStation Legacy Archive...")

    create_legacy_table()

    print("Legacy table created.")

    insert_legacy_items()

    print("Legacy products added.")

    print("Finished successfully!")