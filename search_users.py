import os
import requests

TENANT_URL = os.getenv("CYBERARK_TENANT_URL")
TOKEN = os.getenv("CYBERARK_ACCESS_TOKEN")

if not TENANT_URL or not TOKEN:
    raise EnvironmentError("Missing required environment variables.")

url = f"{TENANT_URL}/CDirectoryService/GetUsers"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "SearchString": "test"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code != 200:
    print("Request failed:", response.text)
    exit(1)

data = response.json()

print(f"Users found: {data.get('Result', {}).get('Count')}")
for user in data.get("Result", {}).get("Results", []):
    row = user.get("Row", {})
    print(f"- {row.get('DisplayName')} ({row.get('Name')})")

