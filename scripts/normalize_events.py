import json
import re
from datetime import datetime

YEAR = 2026

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
    "December": "12",
}

def normalize_date(event):
    date_text = event.get("date", "").strip()

    if not date_text:
        return None

    # Already normalized concert date
    try:
        dt = datetime.strptime(date_text, "%Y-%B-%d")
        return {
            "start_date": dt.strftime("%Y-%m-%d"),
            "end_date": dt.strftime("%Y-%m-%d"),
        }
    except:
        pass

    # October 24th - October 25th, 2026
    m = re.search(
        r"([A-Za-z]+)\s+(\d+)(?:st|nd|rd|th)?\s*-\s*([A-Za-z]+)?\s*(\d+)(?:st|nd|rd|th)?.*?(202\d)",
        date_text,
        re.I
    )

    if m:
        start_month = MONTHS[m.group(1)]
        start_day = m.group(2).zfill(2)

        end_month = MONTHS[m.group(3) or m.group(1)]
        end_day = m.group(4).zfill(2)

        year = m.group(5)

        return {
            "start_date": f"{year}-{start_month}-{start_day}",
            "end_date": f"{year}-{end_month}-{end_day}",
        }

    # Saturday, October 17 ...
    m = re.search(
        r"October\s+(\d+).*?Sunday.*?October\s+(\d+)",
        date_text,
        re.I | re.S
    )

    if m:
        return {
            "start_date": f"{YEAR}-10-{int(m.group(1)):02d}",
            "end_date": f"{YEAR}-10-{int(m.group(2)):02d}",
        }

    # October 1st-3rd 2026
    m = re.search(
        r"October\s+(\d+)(?:st|nd|rd|th)?-(\d+)(?:st|nd|rd|th)?.*?(202\d)",
        date_text,
        re.I
    )

    if m:
        return {
            "start_date": f"{m.group(3)}-10-{int(m.group(1)):02d}",
            "end_date": f"{m.group(3)}-10-{int(m.group(2)):02d}",
        }

    return None


with open("all_events.json") as f:
    events = json.load(f)

normalized = []

for event in events:
    result = normalize_date(event)

    if not result:
        print(f"SKIPPING (needs manual handling): {event['title']}")
        continue

    normalized.append({
        "title": event["title"],
        "location": event.get("location", ""),
        "description": event.get("description", ""),
        "source": event.get("source", ""),
        "start_date": result["start_date"],
        "end_date": result["end_date"],
    })

with open("normalized_events.json", "w") as f:
    json.dump(normalized, f, indent=2)

print(f"Normalized {len(normalized)} events")
