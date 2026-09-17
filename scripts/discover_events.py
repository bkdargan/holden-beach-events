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

print("\nTITLE:")
print(soup.title.text)

print("\nHEADINGS:")

for heading in soup.find_all(["h1", "h2", "h3"])[:20]:
    text = heading.get_text(strip=True)

    if text:
        print(text)
