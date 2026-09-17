import re
import json
import requests

url = "https://holdenbeachnc.com/holden-beach-concert-schedule/"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

text = response.text

pattern = r"(May|June|July|August|September)\s+(\d+)(?:st|nd|rd|th)?-\s+([^<]+)"

matches = re.findall(pattern, text)

events = []

for month, day, band in matches:
    events.append({
        "title": f"Holden Beach Concert - {band.strip()}",
        "month": month,
        "day": day,
        "time": "6:30 PM",
        "location": "Bridgeview Park, Holden Beach NC"
    })

with open("concerts.json", "w") as f:
    json.dump(events, f, indent=2)

print(f"Concerts Found: {len(events)}")
