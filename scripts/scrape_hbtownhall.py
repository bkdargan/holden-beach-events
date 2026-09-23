import json
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
            "location": "Block Q Stage, Holden Beach NC",
            "description": (
                "The Town of Holden Beach offers beginner friendly yoga "
                "classes on Mondays, Wednesdays and Fridays at 10:00 AM."
            ),
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
            "location": "Block Q Stage, Holden Beach NC",
            "description": (
                "Yoga Sculpt combines power yoga and strength training. "
                "Mondays, Wednesdays and Fridays at 9:00 AM."
            ),
            "url": URL,
            "source": "hbtownhall",
            "event_time": "09:00",
            "recurring_pattern": "MWF"
        }
    )

#
# Pickleball
#

if "Pickleball" in text:

    events.append(
        {
            "title": "Programs - Pickleball",
            "location": "Bridgeview Park, Holden Beach NC",
            "description": (
                "Pickleball play on Tuesdays, Thursdays and Saturdays "
                "from 10:00 AM to 1:00 PM."
            ),
            "url": URL,
            "source": "hbtownhall",
            "event_time": "10:00",
            "recurring_pattern": "TTS"
        }
    )

#
# Monster Mash
#

if "Monster Mash Trunk-or-Treat" in text:

    events.append(
        {
            "title": "Monster Mash Trunk-or-Treat",
            "location": "Bridgeview Park, Holden Beach NC",
            "description": (
                "Community trunk-or-treat event."
            ),
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
            "location": "Bridgeview Park, Holden Beach NC",
            "description": (
                "Dog parade, costume contest and fall pictures."
            ),
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
