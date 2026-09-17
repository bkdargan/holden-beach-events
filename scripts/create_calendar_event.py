import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

def normalize(text):
    return (
        text.lower()
        .replace("&", "and")
        .strip()
    )

credentials_json = json.loads(os.environ["GOOGLE_CREDENTIALS"])
calendar_id = os.environ["GOOGLE_CALENDAR_ID"]

credentials = service_account.Credentials.from_service_account_info(
    credentials_json,
    scopes=["https://www.googleapis.com/auth/calendar"]
)

service = build("calendar", "v3", credentials=credentials)

MONTHS = {
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09"
}

with open("concerts.json", "r") as f:
    concerts = json.load(f)

for concert in concerts:

    title = concert["title"]

    month = MONTHS[concert["month"]]
    day = concert["day"].zfill(2)

    start_date = f"2026-{month}-{day}"

    # Search calendar for matching events
    existing_events = service.events().list(
        calendarId=calendar_id,
        q=title,
        singleEvents=True
    ).execute()

    duplicate_found = False

    for existing in existing_events.get("items", []):

        existing_title = existing.get(
            "summary",
            ""
        )

        if normalize(existing_title) == normalize(title):
            duplicate_found = True
            break

    if duplicate_found:
        print(f"SKIPPED (already exists): {title}")
        continue

    event = {
        "summary": title,
        "location": concert["location"],
        "description": (
            "Imported automatically from Holden Beach Concert Schedule\n"
            f"EVENT_ID:{normalize(title)}"
        ),
        "start": {
            "dateTime": f"{start_date}T18:30:00-04:00"
        },
        "end": {
            "dateTime": f"{start_date}T20:00:00-04:00"
        }
    }

    service.events().insert(
        calendarId=calendar_id,
        body=event
    ).execute()

    print(f"CREATED: {title}")
