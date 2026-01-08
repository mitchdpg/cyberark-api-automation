import os
import sys
import requests


def main() -> int:
    tenant_url = os.getenv("CYBERARK_TENANT_URL", "").rstrip("/")
    client_id = os.getenv("CYBERARK_CLIENT_ID")
    client_secret = os.getenv("CYBERARK_CLIENT_SECRET")

    if not tenant_url or not client_id or not client_secret:
        print("Missing required environment variables.", file=sys.stderr)
        print("Expected: CYBERARK_TENANT_URL, CYBERARK_CLIENT_ID, CYBERARK_CLIENT_SECRET", file=sys.stderr)
        return 1

    token_url = f"{tenant_url}/oauth2/platformtoken"

    # Matches your curl: application/x-www-form-urlencoded + client_credentials
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    try:
        r = requests.post(token_url, data=data, timeout=30)
    except requests.RequestException as e:
        print(f"Request error: {e}", file=sys.stderr)
        return 1

    if r.status_code != 200:
        print(f"Token request failed: HTTP {r.status_code}", file=sys.stderr)
        print(r.text, file=sys.stderr)
        return 1

    j = r.json()
    token = j.get("access_token")
    if not token:
        print("No access_token in response:", file=sys.stderr)
        print(j, file=sys.stderr)
        return 1

    # Print only the token so you can capture it easily
    print(token)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
