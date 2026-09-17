import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

credentials_json = json.loads(os.environ["GOOGLE_CREDENTIALS"])
calendar_id = os.environ["GOOGLE_CALENDAR_ID"]

credentials = service_account.Credentials.from_service_account_info(
    credentials_json,
    scopes=["https://www.googleapis.com/auth/calendar"]
)

service = build("calendar", "v3", credentials=credentials)

with open("events.json", "r", encoding="utf-8") as f:
    events = json.load(f)

for e in events:

    title = e.get("title", "Untitled Event")
    description = e.get("description", "")
    url = e.get("url", "")

    event = {
        "summary": title,
        "description": f"{description}\n\nSource: {url}",
        "location": "Brunswick County, NC",
        "start": {
            "date": "2026-09-18"
        },
        "end": {
            "date": "2026-09-19"
        }
    }

    created_event = (
        service.events()
        .insert(calendarId=calendar_id, body=event)
        .execute()
    )

    print(f"Created: {title}")
