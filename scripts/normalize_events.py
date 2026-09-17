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

except FileNotFoundError:
    print("concerts.json not found")

# Hobbs
try:
    with open("hobbs_events.json", "r") as f:
        hobbs = json.load(f)

    for event in hobbs:
        normalized.append({
            "title": event["title"],
            "date": event.get("date_time", ""),
            "location": event.get("location", ""),
            "description": event.get("description", ""),
            "source": "hobbs"
        })

except FileNotFoundError:
    print("hobbs_events.json not found")

# Coastal
try:
    with open("coastal_events.json", "r") as f:
        coastal = json.load(f)

    for event in coastal:
        normalized.append({
            "title": event["title"],
            "date": event.get("date_time", ""),
            "location": event.get("location", ""),
            "description": event.get("description", ""),
            "source": "coastal"
        })

except FileNotFoundError:
    print("coastal_events.json not found")

with open("normalized_events.json", "w") as f:
    json.dump(normalized, f, indent=2)

print(f"Created normalized_events.json with {len(normalized)} events")
