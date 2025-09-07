import requests

websites = (
    "https://google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
)

results = {}

for website in websites:
    if not website.startswith("http"):
        website = f"https://{website}"
    response = requests.get(website)
    if response.status_code >= 500:
        results[website] = "SERVER ERROR"
    elif response.status_code >= 400:
        results[website] = "ERROR"
    elif response.status_code >= 300:
        results[website] = "REDIRECT"
    elif response.status_code >= 200:
        results[website] = "OK"
    elif response.status_code >= 100:
        results[website] = "INFO"
    else:
        results[website] = "ERROR"

print(results)