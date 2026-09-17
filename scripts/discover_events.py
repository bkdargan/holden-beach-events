import requests

sites = [
    "https://www.carolinabreezevacations.com/holden-beach-area-events",
    "https://hbtownhall.com/parks-%26-recreation",
    "https://www.townplanner.com/holden-beach/nc/",
    "https://holdenbeachnc.com/holden-beach-concert-schedule/",
    "https://www.coastalvacationresorts.com/holden-beach-events",
    "https://www.hobbsrealty.com/holden-beach-events",
    "https://www.eventbrite.com/d/nc--holden-beach/events/",
    "https://www.ncbrunswick.com/events/"
]

for site in sites:
    print("\n" + "=" * 80)
    print(site)

    try:
        response = requests.get(
            site,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )

        print("Status Code:", response.status_code)
        print("Length:", len(response.text))

    except Exception as ex:
        print("ERROR:", ex)
