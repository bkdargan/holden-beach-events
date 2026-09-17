import json

all_events = []
seen = set()

# Concerts
try:
    with open("concerts.json", "r") as f:
        concerts = json.load(f)

    for event in concerts:

        key = event["title"].lower().strip()

        if key not in seen:
            seen.add(key)

            event["source"] = "concerts"
            all_events.append(event)

except FileNotFoundError:
    print("concerts.json not found")

# Hobbs
try:
    with open("hobbs_events.json", "r") as f:
        hobbs = json.load(f)

    for event in hobbs:

        key = event["title"].lower().strip()

        if key not in seen:
            seen.add(key)

            event["source"] = "hobbs"
            all_events.append(event)

except FileNotFoundError:
    print("hobbs_events.json not found")

with open("all_events.json", "w") as f:
    json.dump(all_events, f, indent=2)

print(f"Created all_events.json with {len(all_events)} events")
