import requests
from bs4 import BeautifulSoup

SOURCES = [
    {
        "name": "Hobbs Realty",
        "url": "https://www.hobbsrealty.com/holden-beach-events"
    },
    {
        "name": "Coastal Vacation Resorts",
        "url": "https://www.coastalvacationresorts.com/holden-beach-events"
    }
]

for source in SOURCES:

    print("\n" + "=" * 80)
    print(source["name"])

    response = requests.get(
        source["url"],
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    soup = BeautifulSoup(response.text, "html.parser")

    print("\nTITLE:")
    print(soup.title.text)

    print("\nHEADINGS:")

    for heading in soup.find_all(["h1", "h2", "h3"]):
        text = heading.get_text(" ", strip=True)

        if text:
            print(text)
