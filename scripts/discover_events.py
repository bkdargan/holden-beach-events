import requests
from bs4 import BeautifulSoup

url = "https://www.ncbrunswick.com/events/"

html = requests.get(url).text

print("Downloaded page")
print("Length:", len(html))

print("\nSearching for event links...\n")

for line in html.splitlines():
    if "/event/" in line:
        print(line[:300])
        break
