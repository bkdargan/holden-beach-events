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

    location = location.strip()

    return location


def extract_url(url):

    if not url:
        return ""

    match = re.search(
        r'https://[^"\s<]+',
        url
    )

    if match:
        return match.group(0)

    return ""


def extract_dates(event):

    # Concert schedule

    if (
        "month" in event
        and
        "day" in event
    ):

        month = MONTHS.get(
            event["month"]
        )

        if month:

            day = int(
                event["day"]
            )

            return {
                "start_date": (
                    f"2026-{month}-{day:02d}"
                ),
                "end_date": (
                    f"2026-{month}-{day:02d}"
                )
            }

    date_text = (
        event.get(
            "date_time",
            ""
        )
        .strip()
    )

    description = event.get(
        "description",
        ""
    )

    title = event.get(
        "title",
        ""
    )

    # Festival by Sea in description only

    if (
        "October 24-25, 2026"
        in description
    ):

        return {
            "start_date": (
                "2026-10-24"
            ),
            "end_date": (
                "2026-10-25"
            )
        }

    # King Mackerel date hidden in description

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

    if not date_text:
        return None

    # Oct 24-25 style

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

    # Oct 1st-3rd

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

    # Oyster Festival

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

    # Single-day October event

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

    dates = extract
