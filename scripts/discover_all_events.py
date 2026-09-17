import requests
from bs4 import BeautifulSoup

SOURCES = [
    {
        "name": "Holden Beach Concerts",
        "url": "https://holdenbeachnc.com/holden-beach-concert-schedule/"
    },
    {
        "name": "Parks and Recreation",
        "url": "https://hbtownhall.com/parks-%26-recreation"
    },
    {
        "name": "Carolina Breeze",
        "url": "https://www.carolinabreezevacations.com/holden-beach-area-events"
    },
    {
        "name": "Coastal Vacation Resorts",
        "url": "https://www.coastalvacationresorts.com/holden-beach-events"
    },
    {
        "name": "Hobbs Realty",
        "url": "https://www.hobbsrealty.com/holden-beach-events"
    }
]

for source in SOURCES:

    print("\n" + "=" * 80)
    print(source["name"])
    print(source["url"])

    try:

        response = requests.get(
            source["url"],
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        print("Status:", response.status_code)
        print("Length:", len(response.text))

        soup = BeautifulSoup(
