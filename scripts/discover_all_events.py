import requests
from bs4 import BeautifulSoup

url = "https://www.hobbsrealty.com/events/festivals/north-carolina-oyster-festival"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

print("Status:", response.status_code)
print("Length:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

print("\nTITLE:\n")
print(soup.title.text)

print("\nHEADINGS:\n")

for heading in soup.find_all(["h1", "h2", "h3"]):
    text = heading.get_text(" ", strip=True)

    if text:
        print(text)

print("\nFIRST PARAGRAPHS:\n")

count = 0

for p in soup.find_all("p"):

    text = p.get_text(" ", strip=True)

    if len(text) > 40:

        print(text)
        print()

        count += 1

        if count >= 10:
            break
