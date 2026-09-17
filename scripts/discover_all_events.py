import requests
from bs4 import BeautifulSoup

sites = [
    "https://www.hobbsrealty.com/holden-beach-events",
    "https://www.coastalvacationresorts.com/holden-beach-events"
]

for site in sites:

    print("\n" + "=" * 80)
    print(site)

    response = requests.get(
        site,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(response.text, "html.parser")

    print("\nLINKS:\n")

    count = 0

    for link in soup.find_all("a", href=True):

        text = link.get_text(" ", strip=True)

        if (
            "festival" in text.lower()
            or "market" in text.lower()
            or "yoga" in text.lower()
            or "tournament" in text.lower()
            or "tour" in text.lower()
        ):
            print(text)
            print(link["href"])
            print()

            count += 1

            if count >= 20:
                break
