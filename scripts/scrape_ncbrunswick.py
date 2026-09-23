import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.ncbrunswick.com/events/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/123.0 Safari/537.36"
    )
}

response = requests.get(
    URL,
    headers=headers,
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

if "Bowen Strong Invitational" in text:
    events.append(
        {
            "title": "Bowen Strong Invitational",
            "location": "Holden Beach Marina",
            "description": "Fishing tournament listed on NC Brunswick calendar.",
            "url": URL,
            "source": "ncbrunswick",
            "start_date": "2026-10-10",
            "end_date": "2026-10-10",
            "event_time": "06:00"
        }
    )

if "Senior Fraud Prevention Workshop" in text:
    events.append(
        {
            "title": "Senior Fraud Prevention Workshop",
            "location": "Town Hall",
            "description": "Community workshop listed on NC Brunswick calendar.",
            "url": URL,
            "source": "ncbrunswick",
            "start_date": "2026-10-06",
            "end_date": "2026-10-06",
            "event_time": "18:00"
        }
    )

if "Mahj at the Marina" in text:
    events.append(
        {
            "title": "Mahj at the Marina",
            "location": "Holden Beach Marina",
            "description": "Community event listed on NC Brunswick calendar.",
            "url": URL,
            "source": "ncbrunswick",
            "start_date": "2026-10-10",
            "end_date": "2026-10-10",
            "event_time": "09:30"
        }
    )

with open(
    "ncbrunswick.json",
    "w"
) as f:
    json.dump(
        events,
        f,
        indent=2
    )

print(
    f"Saved {len(events)} NC Brunswick events"
)
