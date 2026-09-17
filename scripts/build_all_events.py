import json

all_events = []
seen = set()

def add_events(filename, source):

    try:

        with open(filename, "r") as f:
            events = json.load(f)

        for event in events:

            key = event["title"].lower().strip()

            if key not in seen:

                seen.add(key)

                event["source"] = source

                all_events.append(event)

    except FileNotFoundError:

        print(f"{filename} not found")

add_events("concerts.json", "concerts")
add_events("hobbs_events.json", "hobbs")
add_events("coastal_events.json", "coastal")

with open("all_events.json", "w") as f:
    json.dump(all_events, f, indent=2)

print(f"Created all_events.json with {len(all_events)} events")
