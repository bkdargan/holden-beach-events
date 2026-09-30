import json

normalized = []

# Concerts
try:
    with open("concerts.json", "r") as f:
        concerts = json.load(f)

    for event in concerts:

        normalized.append({
            "title": event["title"],
            "date": f"2026-{event['month']}-{event['day']}",
            "location": event.get("location", ""),
            "description": "",
            "source": "concerts"
        })

except FileNotFoundError
