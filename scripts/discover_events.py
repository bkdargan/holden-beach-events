import re
import requests

url = "https://www.ncbrunswick.com/events/"

html = requests.get(url).text

print("Downloaded page")
print("Length:", len(html))

matches = re.findall(r"/event/[^\"']+", html)

print("\nMatches found:", len(matches))

urls = sorted(set(
    "https://www.ncbrunswick.com" + m
    for m in matches
))

print("\nUnique URLs found:", len(urls))
print()

for url in urls[:20]:
    print(url)
