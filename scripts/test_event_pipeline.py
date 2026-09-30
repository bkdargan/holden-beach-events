import json
from collections import Counter
from datetime import datetime

with open("normalized_events.json", "r") as f:
    events = json.load(f)

months = Counter()
sources = Counter()

dates = []

for event in events:

    sources[event.get("source", "unknown")] += 1

    start_date = event.get("start_date")

    if start_date:

        dt = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        months[dt.strftime("%Y-%m")] += 1

        dates.append(dt)

print("\nEVENT SUMMARY")
print("-" * 40)

print(
    f"Total Events: {len(events)}"
)

if dates:

    print(
        f"Earliest Event: {min(dates).date()}"
    )

    print(
        f"Latest Event: {max(dates).date()}"
    )

print("\nBY SOURCE")
print("-" * 40)

for source, count in sorted(
    sources.items()
):

    print(
        f"{source}: {count}"
    )

print("\nBY MONTH")
print("-" * 40)

for month, count in sorted(
    months.items()
):

    print(
        f"{month}: {count}"
    )
