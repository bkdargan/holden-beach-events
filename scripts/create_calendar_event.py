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


def clean_url(url):

    if not url:
        return ""

    if "https://" not in url:
        return ""

    start = url.find("https://")

    url = url[start:]

    for stop_char in ['"', "<", ">", ","\]:
        if stop_char in url:
            url = url.split(stop_char)[0]

    return url.strip()


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

        for emoji in [
            "🎵 ",
            "🎉 ",
            "🍺 ",
            "🎣 ",
            "🛍️ ",
            "🧘 ",
            "🏝️ "
        \]:
            existing_title = existing_title.replace(
                emoji,
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

    url = clean_url(
        item.get(
            "url",
            ""
        )
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

    event_time = item.get(
        "event_time",
        ""
    )

    #
    # Timed recurring activities
    #

    if event_time:

        start_dt = (
            f"{item['start_date']}"
            f"T{event_time}:00-04:00"
        )

        event = {
            "summary":
                add_emoji(title),
            "location":
                item.get(
                    "location",
                    ""
                ),
            "description":
                full_description,
           start": {
                "dateTime":
                    start_dt
            },
            "end": {
                "dateTime":
                    (
                        datetime.strptime(
                            start_dt,
                            "%Y-%m-%dT%H:%M:%S-04:00"
                        )
                        + timedelta(hours=1)
                    ).strftime(
                        "%Y-%m-%dT%H:%M:%S-04:00"
                    )
            }
        }

    #
    # All-day events
    #

    else:

        event = {
            "summary":
                add_emoji(title),
            "location":
                item.get(
                    "location",
                    ""
                ),
            "description":
                full_description,
            "start": {
                "date":
                    start_date.strftime(
                        "%Y-%m-%d"
                    )
            },
            "end": {
                "date":
                    (
                        end_date +
                        timedelta(days=1)
                    ).strftime(
                        "%Y-%m-%d"
                    )
            }
        }

    if url:

        event["source"] = {
            "title":
                "Official Event Website",
            "url":
                url
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
