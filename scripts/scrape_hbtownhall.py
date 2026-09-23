import json
import re
import requests
from bs4 import BeautifulSoup

URL = "https://hbtownhall.com/parks-%26-recreation"

response = requests.get(
    URL,
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

text = soup.get_text(
    "\n",
    strip=True
)

events = []

#
# Yoga
#

if "Programs - Yoga" in text:

    events.append(
        {
            "title": "Programs - Yoga",
            "location": "Holden Beach",
            "description":
                "Program discovered on Holden Beach Town Hall Parks & Recreation page.",
            "url": URL,
            "source": "hbtownhall",
            "event_time": "10:00",
            "recurring_pattern": "MWF"
        }
    )

#
# Yoga Sculpt
#

if "Programs - Yoga Sculpt" in text:

    events.append(
        {
            "title": "Programs - Yoga Sculpt",
            "location": "Holden Beach",
            "description":
                "Program discovered on Holden Beach Town Hall Parks & Recreation page.",
            "url": URL,
            "source": "hbtownhall",
            "event_time": "09:00",
            "recurring_pattern": "MWF"
        }
    )

#
# Pickleball
#

if "Programs - Pickleball" in text:

    events.append(
        {
            "title": "Programs - Pickleball",
            "location": "Bridgeview Park",
            "description":
                "Open pickleball program.",
            "url": URL,
            "source": "hbtownhall",
            "event_time": "10:00",
            "recurring_pattern": "TTS"
        }
    )

#
# Monster Mash
#

monster_match = re.search(
    r"Monster Mash Trunk-or-Treat",
    text,
    re.IGNORECASE
)

if monster_match:

    events.append(
        {
            "title": "Monster Mash Trunk-or-Treat",
            "location": "Bridgeview Park",
            "description":
                "Community trunk-or-treat event.",
            "url": URL,
            "source": "hbtownhall",
            "start_date": "2026-10-30",
            "end_date": "2026-10-30",
            "event_time": "17:30"
        }
    )

#
# Barktoberfest
#

if "Barktoberfest" in text:

    events.append(
        {
            "title": "Barktoberfest",
            "location": "Bridgeview Park",
            "description":
                "Dog parade and costume contest.",
            "url": URL,
            "source": "hbtownhall",
            "start_date": "2026-10-30",
            "end_date": "2026-10-30",
            "event_time": "16:30"
        }
    )

with open(
    "hbtownhall.json",
    "w"
) as f:

    json.dump(
        events,
        f,
        indent=2
    )

print(
    f"Saved {len(events)} Town Hall events"
)
