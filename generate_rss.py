from feedgen.feed import FeedGenerator
from datetime import datetime, timedelta
import pytz

# =========================================
# CONFIG
# =========================================

TEST_MODE = False

ROME_TZ = pytz.timezone("Europe/Rome")

BASE_URL = "https://UgoMusmeci.github.io/carlentini-rifiuti-rss"

FEED_TITLE = "Comune di Carlentini - Raccolta differenziata"

# =========================================
# NOMI GIORNI E MESI IN ITALIANO
# =========================================

DAY_NAMES = {
    0: "Lunedì",
    1: "Martedì",
    2: "Mercoledì",
    3: "Giovedì",
    4: "Venerdì",
    5: "Sabato",
    6: "Domenica"
}

MONTH_NAMES = {
    1: "gennaio",
    2: "febbraio",
    3: "marzo",
    4: "aprile",
    5: "maggio",
    6: "giugno",
    7: "luglio",
    8: "agosto",
    9: "settembre",
    10: "ottobre",
    11: "novembre",
    12: "dicembre"
}

# =========================================
# CALENDARIO RACCOLTA
# =========================================

WASTE_SCHEDULE = {
    0: (
        "Raccolta Differenziata - esporre umido",
        "Si ricorda di esporre l'umido entro le ore 8:00 di domani."
    ),

    1: (
        "Raccolta Differenziata - esporre carta e cartone",
        "Si ricorda di esporre carta e cartone entro le ore 8:00 di domani."
    ),

    2: (
        "Raccolta Differenziata - esporre vetro e alluminio",
        "Si ricorda di esporre vetro e alluminio entro le ore 8:00 di domani."
    ),

    3: (
        "Raccolta Differenziata - esporre secco residuo",
        "Si ricorda di esporre il secco residuo entro le ore 8:00 di domani."
    ),

    4: (
        "Raccolta Differenziata - esporre la plastica",
        "Si ricorda di esporre la plastica entro le ore 8:00 di domani."
    ),

    5: (
        "Raccolta Differenziata - esporre l'umido",
        "Si ricorda di esporre l'umido entro le ore 8:00 di domani."
    ),

    6: (
        "Raccolta Differenziata - Nessun conferimento",
        "Domani non è previsto alcun conferimento."
    )
}

# =========================================
# DATA
# =========================================

now = datetime.now(ROME_TZ)

tomorrow = now + timedelta(days=1)

weekday = tomorrow.weekday()

# =========================================
# TEST MODE
# =========================================

if TEST_MODE:

    current_time = now.strftime("%H:%M")

    title = f"🧪 TEST RSS {current_time}"

    description = (
        f"Test automatico feed RSS Comuni-Chiamo - "
        f"{now.strftime('%d/%m/%Y %H:%M:%S')}"
    )

    unique_id = now.strftime("%Y%m%d%H%M%S")

else:

    waste_title, description = WASTE_SCHEDULE[weekday]

    day_name = DAY_NAMES[weekday]

    formatted_date = (
        f"{day_name} "
        f"{tomorrow.day} "
        f"{MONTH_NAMES[tomorrow.month]}"
    )

    title = f"{waste_title} - {formatted_date}"

    unique_id = (
        f"{tomorrow.strftime('%Y%m%d')}-"
        f"{weekday}"
    )

# =========================================
# GENERAZIONE FEED
# =========================================

fg = FeedGenerator()

fg.title(FEED_TITLE)

fg.link(href=BASE_URL)

fg.description(
    "Feed automatico raccolta differenziata Comune di Carlentini"
)

fg.language("it")

# =========================================
# ITEM
# =========================================

fe = fg.add_entry()

entry_link = (
    "https://www.aziendaspecialecarlentini.it/"
    "wp-content/uploads/2026/05/Carlentini-min.pdf"
)

fe.id(entry_link)

fe.title(title)

fe.description(description)

fe.link(href=entry_link)

fe.pubDate(now)

# =========================================
# OUTPUT
# =========================================

fg.rss_file("feed.xml")

print("Feed RSS generato correttamente.")