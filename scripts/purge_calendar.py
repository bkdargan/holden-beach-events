import os
from datetime import datetime, timezone
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

creds = Credentials(
    None,
    refresh_token=os.environ["GOOGLE_REFRESH_TOKEN"],
    client_id=os.environ["GOOGLE_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
    token_uri="https://oauth2.googleapis.com/token"
)

service = build("calendar", "v3", credentials=creds)

CALENDAR_ID = os.environ["GOOGLE_CALENDAR_ID"]

start = datetime.now(timezone.utc).isoformat()
end = datetime(2026, 12, 31, 23, 59, tzinfo=timezone.utc).isoformat()

print(f"Purging events from {start} to {end} in calendar: {CALENDAR_ID}")

events = service.events().list(
    calendarId=CALENDAR_ID,
    timeMin=start,
    timeMax=end,
    singleEvents=True
).execute().get("items", [])

print(f"Found {len(events)} events to delete.")

for event in events:
    event_id = event["id"]
    summary = event.get("summary", "No Title")
    print(f"Deleting: {summary} ({event_id})")
    service.events().delete(
        calendarId=CALENDAR_ID,
        eventId=event_id
    ).execute()

print("All events deleted.")

FILE_TO_DELETE = "docs/holden-beach-events.ics"

if os.path.exists(FILE_TO_DELETE):
    os.remove(FILE_TO_DELETE)
    print(f"Deleted file: {FILE_TO_DELETE}")
else:
    print(f"File not found: {FILE_TO_DELETE}")
