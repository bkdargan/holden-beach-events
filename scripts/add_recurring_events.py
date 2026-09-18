import json
from datetime import datetime, timedelta

with open("normalized_events.json", "r") as f:
    events = json.load(f)

# Yoga at Bridgeview Park
start = datetime(2026, 1, 1)
end = datetime(2026, 12, 31)

current = start

while current <= end:

    if current.weekday() in [0, 2, 4]:
        events.append(
            {
                "title": "Yoga at Bridgeview Park",
                "location": "Bridgeview Park, Holden Beach NC",
                "description": (
                    "Beginner friendly yoga class taught by Alice Ledford. "
                    "Mondays, Wednesdays and Fridays at 9:00 AM."
                ),
                "url": "",
                "source": "hobbs-recurring",
                "start_date": current.strftime("%Y-%m-%d"),
                "end_date": current.strftime("%Y-%m-%d")
            }
        )

    current += timedelta(days=1)

# Sunset Beach Market
start = datetime(2026, 4, 30)
end = datetime(2026, 9, 24)

current = start

while current <= end:

    if current.weekday() == 3:
        events.append(
            {
                "title": "Sunset Beach Market at the Park",
                "location": "Sunset Beach Town Park",
                "description": (
                    "Weekly summer market. "
                    "Thursdays 9:00 AM - 1:00 PM."
                ),
                "url": "",
                "source": "hobbs-recurring",
                "start_date": current.strftime("%Y-%m-%d"),
                "end_date": current.strftime("%Y-%m-%d")
            }
        )

    current += timedelta(days=1)

# Bald Head Island Guided Historic Tours
start = datetime(2026, 3, 1)
end = datetime(2026, 12, 31)

current = start

while current <= end:

    if current.weekday() in [1, 4, 5]:
        events.append(
            {
                "title": "Bald Head Island Guided Historic Tours",
                "location": "Bald Head Island",
                "description": (
                    "Guided historic golf cart tour."
                ),
                "url": "",
                "source": "coastal-recurring",
                "start_date": current.strftime("%Y-%m-%d"),
                "end_date": current.strftime("%Y-%m-%d")
            }
        )

    current += timedelta(days=1)

with open("normalized_events.json", "w") as f:
    json.dump(events, f, indent=2)

print(f"Final event count: {len(events)}")
