# CyberArk API Automation (Python)

Built scripts to authenticate with CyberArk Identity APIs using OAuth client credentials, generate bearer tokens, and perform authenticated identity attribute queries for user and access workflows. 
Requires valid CyberArk identity credentials (api user assigned to OAuth app), and a user UUID for lookups. Live testing depends on tenant access.

---

## Security Note

This project uses environment variables for authentication.  
No secrets, tokens, or tenant-specific identifiers are stored in the repository.  
All examples use placeholder values.

---

## Overview

This project demonstrates lightweight Python automation using CyberArk Identity APIs. It focuses on authenticating via OAuth 2.0 client credentials, generating a bearer access token, and performing authenticated API calls to retrieve user identity information.

The goal of this project is not full application development, but practical security automation commonly used in presales evaluations, proof-of-concept work, and identity integrations.

---

## What This Project Demonstrates

- OAuth 2.0 client credentials authentication
- Secure bearer token generation
- Use of environment variables for secret handling
- Authenticated REST API calls
- Retrieval of identity and user attributes
- Practical automation patterns for identity security workflows

---

## Project Structure

```
cyberark-api-automation/
├── get_token.py        # Generates OAuth bearer token
├── get_user.py         # Retrieves user attributes via 'GetUser' api endpoint for a specific user
├── search_users.py     # Retrieves all users via the 'GetUsers' api endpoint
├── requirements.txt
└── README.md
```

## Additional Script: User Search (GetUsers API Endpoint)

This project also includes a user search script that demonstrates querying CyberArk Identity for users matching a search string.

### search_users.py
- Accepts a search term as a command-line argument
- Uses a bearer token generated via OAuth 2.0 client credentials
- Returns a count of matching users and basic identity attributes

Example usage:

```bash
export CYBERARK_ACCESS_TOKEN="$(python3 get_token.py)"
python3 search_users.py "mitchell"
```

Example Output: Users found: 5


---

## Use Case

This project reflects common real-world identity automation scenarios, such as:
- Validating API access during security evaluations
- Automating identity lookups
- Supporting presales demonstrations and proofs of concept
- Testing identity integrations in a controlled environment

---

## Disclaimer

This project is not affiliated with or officially supported by CyberArk.  
It was created for learning and demonstration purposes using a trial environment.


