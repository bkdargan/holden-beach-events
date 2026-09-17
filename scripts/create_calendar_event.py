import json
import os

creds = os.environ["GOOGLE_CREDENTIALS"]
calendar_id = os.environ["GOOGLE_CALENDAR_ID"]

print("Google credentials loaded")
print(f"Calendar ID length: {len(calendar_id)}")

event = {
    "summary": "Holden Beach Automation Test",
    "location": "Holden Beach, NC",
    "description": "Created automatically by GitHub Actions"
}

print("Event ready:")
print(json.dumps(event, indent=2))
