import json
import re
from datetime import datetime

OUTPUT_FILE = "normalized_events.json"

MONTHS = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}


def extract_dates(event):

    # Concert events
    if "month" in event and "day" in event:

        month = MONTHS.get(event["month"])

        if month:

            return {
                "start_date": f"2026-{month}-{int(event['day']):02d}",
                "end_date": f"2026-{month}-{int(event['day']):02d}"
            }

    date_text = event.get("date_time", "").strip()
    description = event.get("description", "")

    if not date_text:

        # Festival by Sea date buried in description
        if "October 24-25, 2026" in description:
            return {
                "start_date": "2026-10-24",
                "end_date": "2026-10-25"
            }

        return None

    # October 24th - October 25th, 2026

    m = re.search(
        r"([A-Za-z]+)\s+(\d+)(?:st|nd|rd|th)?\s*-\s*([A-Za-z]+)?\s*(\d+)(?:st|nd|rd|th)?.*?(202\d)",
        date_text,
        re.IGNORECASE
    )

    if m:

        start_month = datetime.strptime(
            m.group(1),
            "%B"
        ).month

        end_month = start_month

        if m.group(3):

            end_month = datetime.strptime(
                m.group(3),
                "%B"
            ).month

        return {
            "start_date": f"{m.group(5)}-{start_month:02d}-{int(m.group(2)):02d}",
            "end_date": f"{m.group(5)}-{end_month:02d}-{int(m.group(4)):02d}"
        }

    # October 1st-3rd 2026

    m = re.search(
        r"October\s+(\d+)(?:st|nd|rd|th)?-(\d+)(?:st|nd|rd|th)?.*?(202\d)",
        date_text,
        re.IGNORECASE
    )

    if m:

        return {
            "start_date": f"{m.group(3)}-10-{int(m.group(1)):02d}",
            "end_date": f"{m.group(3)}-10-{int(m.group(2)):02d}"
        }

    # Oyster Festival

    if "October" in date_text and "Sunday" in date_text:

        numbers = re.findall(
            r"October\s+(\d+)",
            date_text
        )

        if len(numbers) >= 2:

            return {
                "start_date": f"2026-10-{int(numbers[0]):02d}",
                "end_date": f"2026-10-{int(numbers[1]):02d}"
            }

    # Single day event

    m = re.search(
        r"October\s+(\d+)",
        date_text,
        re.IGNORECASE
    )

    if m:

        return {
            "start_date": f"2026-10-{int(m.group(1)):02d}",
            "end_date": f"2026-10-{int(m.group(1)):02d}"
        }

    return None


with open("all_events.json", "r") as f:
    all_events = json.load(f)

normalized = []
skipped = []

for event in all_events:

    dates = extract_dates(event)

    if not dates:

        skipped.append(event["title"])

        continue

    normalized.append(
        {
            "title": event["title"],
            "location": event.get("location", ""),
            "description": event.get("description", ""),
            "source": event.get("source", ""),
            "start_date": dates["start_date"],
            "end_date": dates["end_date"]
        }
    )

with open(OUTPUT_FILE, "w") as f:

    json.dump(
        normalized,
        f,
        indent=2
    )

print()
print(f"Normalized events: {len(normalized)}")
print(f"Skipped events: {len(skipped)}")
print()

for event in skipped:
    print(f"SKIPPED: {event}")
