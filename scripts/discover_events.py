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

print("\nLOOKING FOR DATE INFORMATION\n")

page_text = soup.get_text("\n")

for line in page_text.splitlines():
    line = line.strip()

    if line:
        if (
            "2026" in line
            or "May" in line
            or "June" in line
            or "July" in line
            or "August" in line
            or "September" in line
            or "October" in line
        ):
            print(line)
