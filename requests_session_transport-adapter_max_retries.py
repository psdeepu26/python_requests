#requests with max retries with Sessions

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

session.mount('https://api.github.com',github_adapter)

try:
    response = session.get('https://api.github.com')
except ConnectionError as ce:
    print(f"{ce}")
else:
    print(f"Sucesss!! {response.status_code}")
