from feedgen.feed import FeedGenerator
from datetime import datetime
import pytz
import random
import os

# =========================================
# CONFIG
# =========================================

TEST_MODE = True

ROME_TZ = pytz.timezone("Europe/Rome")

BASE_URL = "https://UgoMusmeci.github.io/carlentini-rifiuti-rss"

FEED_TITLE = "Comune di Carlentini - Raccolta differenziata"

# =========================================
# CALENDARIO RACCOLTA
# =========================================

WASTE_SCHEDULE = {
    0: ("🍂 Umido", "Si ricorda di esporre l'umido entro le ore 6:00-8:00."),
    1: ("📦 Carta e cartone", "Si ricorda di esporre carta e cartone entro le ore 6:00-8:00."),
    2: ("♻️ Vetro e alluminio", "Si ricorda di esporre vetro e alluminio entro le ore 6:00-8:00."),
    3: ("🗑️ Secco residuo", "Si ricorda di esporre il secco residuo entro le ore 6:00-8:00."),
    4: ("🟡 Plastica", "Si ricorda di esporre la plastica entro le ore 6:00-8:00."),
    5: ("🍂 Umido", "Si ricorda di esporre l'umido entro le ore 6:00-8:00."),
    6: ("✅ Nessun conferimento", "Domani non è previsto alcun conferimento.")
}

# =========================================
# DATA
# =========================================

now = datetime.now(ROME_TZ)

weekday = now.weekday()

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

    title, description = WASTE_SCHEDULE[weekday]

    unique_id = now.strftime("%Y%m%d")

# =========================================
# GENERAZIONE FEED
# =========================================

fg = FeedGenerator()

fg.title(FEED_TITLE)

fg.link(href=BASE_URL)

fg.description("Feed automatico raccolta differenziata Comune di Carlentini")

fg.language("it")

# ITEM
fe = fg.add_entry()

entry_link = f"{BASE_URL}/news/{unique_id}"

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