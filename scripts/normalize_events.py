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


def clean_location(location):

    if not location:
        return ""

    location = re.sub(
        r"^When:\s*",
        "",
        location,
        flags=re.IGNORECASE
    )

    location = re.sub(
        r"Website$",
        "",
        location,
        flags=re.IGNORECASE
    )

    return location.strip()


def extract_url(url_text):

    if not url_text:
        return ""

    match = re.search(
        r"https://[^\s\"<>]+",
        url_text
    )

    if match:
        return match.group(0)

    return ""


def extract_dates(event):

    if (
        "month" in event
        and
        "day" in event
    ):

        month = MONTHS.get(
            event["month"]
        )

        if month:

            return {
                "start_date":
                    f"2026-{month}-{int(event['day']):02d}",
                "end_date":
                    f"2026-{month}-{int(event['day']):02d}"
            }

    title = event.get(
        "title",
        ""
    )

    description = event.get(
        "description",
        ""
    )

    date_text = event.get(
        "date_time",
        ""
    )

    if (
        title ==
        "U.S. Open King Mackerel Tournament"
    ):

        return {
            "start_date":
                "2026-10-01",
            "end_date":
                "2026-10-03"
        }

    if (
        "October 24-25, 2026"
        in description
    ):

        return {
            "start_date":
                "2026-10-24",
            "end_date":
                "2026-10-25"
        }

    if not date_text:
        return None

    m = re.search(
        r"([A-Za-z]+)\s+(\d+)"
        r"(?:st|nd|rd|th)?\s*-\s*"
        r"([A-Za-z]+)?\s*(\d+)"
        r"(?:st|nd|rd|th)?.*?"
        r"(202\d)",
        date_text,
        re.IGNORECASE
    )

    if m:

        start_month = (
            datetime.strptime(
                m.group(1),
                "%B"
            ).month
        )

        end_month = start_month

        if m.group(3):

            end_month = (
                datetime.strptime(
                    m.group(3),
                    "%B"
                ).month
            )

        return {
            "start_date":
                f"{m.group(5)}-{start_month:02d}-{int(m.group(2)):02d}",
            "end_date":
                f"{m.group(5)}-{end_month:02d}-{int(m.group(4)):02d}"
        }

    m = re.search(
        r"October\s+(\d+)"
        r"(?:st|nd|rd|th)?"
        r"-(\d+)"
        r"(?:st|nd|rd|th)?.*?"
        r"(202\d)",
        date_text,
        re.IGNORECASE
    )

    if m:

        return {
            "start_date":
                f"{m.group(3)}-10-{int(m.group(1)):02d}",
            "end_date":
                f"{m.group(3)}-10-{int(m.group(2)):02d}"
        }

    if (
        "October" in date_text
        and
        "Sunday" in date_text
    ):

        numbers = re.findall(
            r"October\s+(\d+)",
            date_text
        )

        if len(numbers) >= 2:

            return {
                "start_date":
                    f"2026-10-{int(numbers[0]):02d}",
                "end_date":
                    f"2026-10-{int(numbers[1]):02d}"
            }

    m = re.search(
        r"October\s+(\d+)",
        date_text,
        re.IGNORECASE
    )

    if m:

        day = int(
            m.group(1)
        )

        return {
            "start_date":
                f"2026-10-{day:02d}",
            "end_date":
                f"2026-10-{day:02d}"
        }

    return None


with open(
    "all_events.json",
    "r"
) as f:

    all_events = json.load(f)

normalized = []
skipped = []
seen = set()

for event in all_events:

    dates = extract_dates(event)

    if not dates:

        skipped.append(
            event["title"]
        )

        continue

    key = (
        event["title"]
        .lower()
        .strip()
    )

    if key in seen:
        continue

    seen.add(key)

    normalized.append(
        {
            "title": event["title"],
            "location":
                clean_location(
                    event.get(
                        "location",
                        ""
                    )
                ),
            "description":
                event.get(
                    "description",
                    ""
                ),
            "url":
                extract_url(
                    event.get(
                        "url",
                        ""
                    )
                ),
            "source":
                event.get(
                    "source",
                    ""
                ),
            "start_date":
                dates["start_date"],
            "end_date":
                dates["end_date"]
        }
    )

with open(
    OUTPUT_FILE,
    "w"
) as f:

    json.dump(
        normalized,
        f,
        indent=2
    )

print()
print(
    f"Normalized events: {len(normalized)}"
)
print(
    f"Skipped events: {len(skipped)}"
)
print()

for event in skipped:
    print(
        f"SKIPPED: {event}"
    )
