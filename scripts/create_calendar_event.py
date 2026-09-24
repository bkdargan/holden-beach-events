import json
import os
from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build

#
# CALENDAR SETTINGS
#
IMPORT_WINDOW_DAYS = 10

TIMEZONE = "America/New_York"


def build_event_key(item):

    return (
        f"{item['title']}|"
        f"{item['start_date']}|"
        f"{item.get('event_time', '')}"
    )


def add_emoji(title):

    lower = title.lower()

    if "concert" in lower:
        return f"🎵 {title}"

    if "festival" in lower:
        return f"🎉 {title}"

    if "wine" in lower or "beer" in lower:
        return f"🍺 {title}"

    if "mackerel" in lower:
        return f"🎣 {title}"

    if "market" in lower:
        return f"🛍️ {title}"

    if "yoga" in lower:
        return f"🧘 {title}"

    if "pickleball" in lower:
        return f"🏓 {title}"

    if "tour" in lower:
        return f"🏝️ {title}"

    return title

credentials_json = json.loads(
    os.environ["GOOGLE_CREDENTIALS"]
)

calendar_id = os.environ[
    "GOOGLE_CALENDAR_ID"
]

credentials = (
    service_account.Credentials
    .from_service_account_info(
        credentials_json,
        scopes=[
            "https://www.googleapis.com/auth/calendar"
        ]
    )
)

service = build(
    "calendar",
    "v3",
    credentials=credentials
)
#
# LOAD EXISTING SCRIPT-CREATED EVENTS
#

existing_keys = set()

calendar_events = service.events().list(
    calendarId=calendar_id,
    maxResults=2500,
    singleEvents=True
).execute()

for existing_event in calendar_events.get(
    "items",
    []
):

    description = existing_event.get(
        "description",
        ""
    )

    if "EVENT_KEY:" in description:

        for line in description.splitlines():

            if line.startswith(
                "EVENT_KEY:"
            ):

                existing_keys.add(
                    line.replace(
                        "EVENT_KEY:",
                        ""
                    ).strip()
                )
with open(
    "normalized_events.json",
    "r"
) as f:

    events = json.load(f)

print()
print(
    f"Found {len(events)} normalized events"
)

print(
    f"Import window: {IMPORT_WINDOW_DAYS} days"
)

print()

created = 0

today = datetime.now()

window_end = (
    today +
    timedelta(days=IMPORT_WINDOW_DAYS)
)

for item in events:

    event_date = datetime.strptime(
        item["start_date"],
        "%Y-%m-%d"
    )

    #
    # ONLY INCLUDE EVENTS IN IMPORT WINDOW
    #
    title = item["title"]

    event_key = build_event_key(
        item
    )

    if event_key in existing_keys:

        print(
            f"SKIPPED (duplicate): {title}"
        )

        continue

    description = item.get(
        "description",
        ""
    )

    source_name = item.get(
        "source",
        ""
    )

    url = item.get(
        "url",
        ""
    )

    full_description = (
        description +
        f"\n\nEVENT_KEY:{event_key}"
    )
    if event_date < today:
        continue

    if event_date > window_end:
        continue
    if source_name:

        full_description += (
            f"\n\nSource: {source_name}"
        )

    if url:

        full_description += (
            f"\n\nMore Information:\n{url}"
        )

    start_date = datetime.strptime(
        item["start_date"],
        "%Y-%m-%d"
    )

    end_date = datetime.strptime(
        item["end_date"],
        "%Y-%m-%d"
    )

    event_time = item.get(
        "event_time",
        ""
    )

    #
    # TIMED EVENTS
    #

    if event_time:

        start_dt = datetime.strptime(
            f"{item['start_date']} {event_time}",
            "%Y-%m-%d %H:%M"
        )

        end_dt = start_dt + timedelta(
            hours=1
        )

        event = {
            "summary": add_emoji(title),
            "location": item.get(
                "location",
                ""
            ),
            "description": full_description,
            "start": {
                "dateTime": start_dt.isoformat(),
                "timeZone": TIMEZONE
            },
            "end": {
                "dateTime": end_dt.isoformat(),
                "timeZone": TIMEZONE
            }
        }

    #
    # ALL-DAY EVENTS
    #

    else:

        event = {
            "summary": add_emoji(title),
            "location": item.get(
                "location",
                ""
            ),
            "description": full_description,
            "start": {
                "date": start_date.strftime(
                    "%Y-%m-%d"
                )
            },
            "end": {
                "date": (
                    end_date +
                    timedelta(days=1)
                ).strftime(
                    "%Y-%m-%d"
                )
            }
        }

    service.events().insert(
        calendarId=calendar_id,
        body=event
    ).execute()

    created += 1

    print(
        f"CREATED: {title}"
    )

print()
print(
    f"Created: {created}"
)
print()
