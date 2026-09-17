import re
import requests

url = "https://holdenbeachnc.com/holden-beach-concert-schedule/"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

text = response.text

pattern = r"(May|June|July|August|September)\s+\d+(?:st|nd|rd|th)?-\s+(.+)"

matches = re.findall(pattern, text)

print("Concerts Found:", len(matches))
print()

for month, band in matches:
    print(month, "-", band)
