# Get request to perform status code check

import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print("Sucesss!!")
elif response.status_code == 404:
    print("Failure!")
