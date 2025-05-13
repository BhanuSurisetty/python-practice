#External modules
"""
print(response.status_code)
This prints the HTTP status code returned by the server.

Common status codes:

200 → Success (OK)

301 → Redirected

403 → Forbidden

404 → Not Found

500 → Internal Server Error
"""

import requests
response = requests.get('https://github.com/')
print(response.status_code)

