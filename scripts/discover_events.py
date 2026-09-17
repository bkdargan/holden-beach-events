import requests

url = "https://www.ncbrunswick.com/events/"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status Code:", response.status_code)
print("Final URL:", response.url)
print("Length:", len(response.text))

print("\nFIRST 1000 CHARACTERS:\n")
print(response.text[:1000])
