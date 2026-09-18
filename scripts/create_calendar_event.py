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

        existing_title = (
            existing_title
            .replace("🎵 ", "")
            .replace("🎉 ", "")
            .replace("🍺 ", "")
            .replace("🎣 ", "")
            .replace("🛍️ ", "")
            .replace("🧘 ", "")
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

    url = item.get(
        "url",
        ""
    )

    description = item.get(
        "description",
        ""
    )

    source_name = item.get(
        "source",
        ""
    )

    full_description = description

    if source_name:

        full_description += (
            f"\n\nSource: {source_name}"
        )

    if url:

        full_description += (
            f"\n\nMore Information:\n{url}"
        )

    full_description += (
        f"\n\nEVENT_ID:{normalize(title)}"
    )

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

    if url:

        event["source"] = {
            "title": "Event Website",
            "url": url
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
