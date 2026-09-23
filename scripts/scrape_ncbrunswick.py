import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.ncbrunswick.com/events/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)

print(f"Status Code: {response.status_code}")

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

text = soup.get_text(
    "\n",
    strip=True
)

with open(
    "ncbrunswick_raw.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

events = []

with open(
    "ncbrunswick.json",
    "w"
) as f:
    json.dump(
        events,
        f,
        indent=2
    )

print(
    f"Saved raw page text ({len(text)} characters)"
)

print(
    f"Saved {len(events)} NC Brunswick events"
)
