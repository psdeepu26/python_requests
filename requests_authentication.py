# Get or Post with Authentication

import requests
from getpass import getpass
username = input("Enter Username: ")

response = requests.get(
    url = 'https://api.github.com',
    auth = (username, getpass())
)

if response:
    print("Success!")
else:
    print("Failure")
