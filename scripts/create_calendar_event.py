import json
import os
from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build


def normalize(text):
    return (
        text.lower()
        .replace("&", "and")
        .strip()
    )


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

with open(
    "normalized_events.json",
    "r"
) as f:

    events = json.load(f)

print()
print(
    f"Found {len(events)} normalized events"
)
print()

created = 0
skipped = 0

for item in events:

    title = item["title"]

    existing_events = (
        service.events()
        .list(
            calendarId=calendar_id,
            q=title,
            singleEvents=True
        )
        .execute()
    )

    duplicate_found = False

    for existing in existing_events.get(
        "items",
        []
    ):

        existing_title = existing.get(
            "summary",
            ""
        )

        if (
            normalize(existing_title)
            ==
            normalize(title)
        ):
            duplicate_found = True
            break

    if duplicate_found:

        skipped += 1

        print(
            f"SKIPPED: {title}"
        )

        continue

    start_date = datetime.strptime(
        item["start_date"],
        "%Y-%m-%d"
    )

    end_date = datetime.strptime(
        item["end_date"],
        "%Y-%m-%d"
    )

    event = {
        "summary": title,
        "location": item.get(
            "location",
            ""
        ),
        "description": (
            f"{item.get('description', '')}\n\n"
            f"Source: {item.get('source', '')}\n"
            f"EVENT_ID:{normalize(title)}"
        ),
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
print(
    f"Skipped: {skipped}"
)
print()
