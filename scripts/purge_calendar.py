import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

#
# AUTHENTICATION
#

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

print()
print(f"Calendar: {calendar_id}")
print()

#
# LOAD EVENTS
#

deleted = 0
page_token = None

while True:

    results = service.events().list(
        calendarId=calendar_id,
        maxResults=2500,
        pageToken=page_token,
        singleEvents=True
    ).execute()

    events = results.get(
        "items",
        []
    )

    for event in events:

        description = event.get(
            "description",
            ""
        )

        #
        # ONLY DELETE EVENTS CREATED
        # BY THIS PROJECT
        #

        if "EVENT_KEY:" not in description:
            continue

        summary = event.get(
            "summary",
            "No Title"
        )

        event_id = event["id"]

        print(
            f"Deleting: {summary}"
        )

        service.events().delete(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()

        deleted += 1

    page_token = results.get(
        "nextPageToken"
    )

    if not page_token:
        break

print()
print(
    f"Deleted {deleted} calendar events."
)
print()
