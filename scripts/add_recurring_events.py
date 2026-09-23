import json
from datetime import datetime, timedelta

with open("normalized_events.json", "r") as f:
    events = json.load(f)

today = datetime.now()

end_date = today + timedelta(days=20)

#
# Yoga at Bridgeview Park
#

current = today

while current <= end_date:

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
                "event_time": "09:00",
                "start_date": current.strftime("%Y-%m-%d"),
                "end_date": current.strftime("%Y-%m-%d")
            }
        )

    current += timedelta(days=1)

#
# Sunset Beach Market
#

current = today

while current <= end_date:

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
                "event_time": "09:00",
                "start_date": current.strftime("%Y-%m-%d"),
                "end_date": current.strftime("%Y-%m-%d")
            }
        )

    current += timedelta(days=1)

#
# Bald Head Island Guided Historic Tours
#

current = today

while current <= end_date:

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
                "event_time": "10:00",
                "start_date": current.strftime("%Y-%m-%d"),
                "end_date": current.strftime("%Y-%m-%d")
            }
        )

    current += timedelta(days=1)

with open("normalized_events.json", "w") as f:
    json.dump(events, f, indent=2)

print(f"Final event count: {len(events)}")
