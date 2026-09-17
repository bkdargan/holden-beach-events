import json
import requests
from bs4 import BeautifulSoup

BASE = "https://www.coastalvacationresorts.com"

links = [
    "/holden-beach-events/outdoor-activities/bald-head-island-guided-historic-tours",
    "/holden-beach-events/events/us-open-king-mackerel-tournament",
    "/holden-beach-events/festivals/north-carolina-oyster-festival",
    "/holden-beach-events/festivals/lighthouse-beer-wine-festival",
    "/holden-beach-events/festivals/festival-sea-holden-beach"
]

events = []

for link in links:

    url = BASE + link

    print(f"Checking: {url}")

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    soup = BeautifulSoup(response.text, "html.parser")

    title = ""

    h1 = soup.find("h1")

    if h1:
        title = h1.get_text(" ", strip=True)

    paragraphs = []

    for p in soup.find_all("p"):
        text = p.get_text(" ", strip=True)

        if len(text) > 30:
            paragraphs.append(text)

    description = paragraphs[0] if paragraphs else ""

    location = ""
    date_time = ""

    for p in paragraphs:

        if "Where:" in p:
            location = p.replace("Where:", "").strip()

        if "When:" in p:
            date_time = p.replace("When:", "").strip()

    events.append({
        "title": title,
        "date_time": date_time,
        "location": location,
        "description": description,
        "url": url
    })

with open("coastal_events.json", "w") as f:
    json.dump(events, f, indent=2)

print(f"Created coastal_events.json with {len(events)} events")
`
