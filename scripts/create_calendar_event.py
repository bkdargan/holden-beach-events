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

event = {
    "summary": "Holden Beach Automation Test",
    "location": "Holden Beach, NC",
    "description": "Created automatically by GitHub Actions",
    "start": {
        "dateTime": "2026-09-18T10:00:00-04:00"
    },
    "end": {
        "dateTime": "2026-09-18T11:00:00-04:00"
    }
}

created_event = service.events().insert(
    calendarId=calendar_id,
    body=event
).execute()

print("SUCCESS")
print(created_event.get("htmlLink"))
