# Using Sessions for persistant paramenters across requests

import requests
from requests.exceptions import HTTPError
from getpass import getpass

username = input("Enter Username: ")

with requests.Session() as session:
    session.auth = (username, getpass())

try:
    response = session.get(url='https://api.github.com')
    response.raise_for_status()
except HTTPError as httperror:
    print(f"{httperror}")
except Exception as error:
    print(f"{error}")
else:
    print(f"Success for {username}")
