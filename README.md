# CyberArk API Automation (Python)

Built scripts to authenticate with CyberArk Identity APIs using OAuth client credentials, generate bearer tokens, and perform authenticated identity attribute queries for user and access workflows.

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
├── get_user.py         # Retrieves user identity data
├── requirements.txt
└── README.md
```


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


