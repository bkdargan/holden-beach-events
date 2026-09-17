import json
import requests
from bs4 import BeautifulSoup

BASE = "https://www.hobbsrealty.com"

links = [
    "/events/festivals/north-carolina-oyster-festival",
    "/events/festivals/north-carolina-festival-sea-holden-beach",
    "/events/festivals/yoga-bridgeview-park",
    "/events/weekly-events/sunset-beach-market-park",
    "/events/sports-competitions/us-open-king-mackerel-tournament"
]

events = []

for link in links:

    url = BASE + link

    print("Checking:", url)

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(response.text, "html.parser")

    title = ""

    h1 = soup.find("h1")

    if h1:
        title = h1.get_text(" ", strip=True)

    events.append({
        "title": title,
        "url": url
    })

with open("hobbs_events.json", "w") as f:
    json.dump(events, f, indent=2)

print("Created hobbs_events.json")
      - name: Show hobbs_events.json
        run: |
          cat hobbs_events.json
