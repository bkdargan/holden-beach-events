import requests
from bs4 import BeautifulSoup

URL = "https://hbtownhall.com/parks-%26-recreation"

response = requests.get(
    URL,
    timeout=30
)

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
    "hbtownhall_raw.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(text)

print("Saved raw page text")
print(f"Length: {len(text)} characters")
