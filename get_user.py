import os
import sys
import requests


def main() -> int:
    tenant_url = os.getenv("CYBERARK_TENANT_URL", "").rstrip("/")
    token = os.getenv("CYBERARK_ACCESS_TOKEN")

    if not tenant_url or not token:
        print("Missing CYBERARK_TENANT_URL or CYBERARK_ACCESS_TOKEN", file=sys.stderr)
        return 1

    url = f"{tenant_url}/CDirectoryService/GetUser"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Use the API user UUID you already tested
    payload = {
        "ID": "USER_UUID_HERE"
    }

    r = requests.post(url, json=payload, headers=headers, timeout=30)

    if r.status_code != 200:
        print(f"Request failed: HTTP {r.status_code}", file=sys.stderr)
        print(r.text, file=sys.stderr)
        return 1

    print(r.json())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

