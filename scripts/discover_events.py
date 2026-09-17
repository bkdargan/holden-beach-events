import requests
from bs4 import BeautifulSoup

url = "https://holdenbeachnc.com/holden-beach-concert-schedule/"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("Status:", response.status_code)
print("Length:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

print("\nTABLES FOUND:", len(soup.find_all("table")))

print("\nHEADINGS:")

for heading in soup.find_all(["h1", "h2", "h3"]):
    text = heading.get_text(strip=True)

    if text:
        print(text)

print("\nFIRST 20 ROWS:\n")

for row in soup.find_all("tr")[:20]:
    print(row.get_text(" | ", strip=True))
