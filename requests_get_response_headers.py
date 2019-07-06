# Get request to get the header information which is by default json formatted which is also not case sensitive

import requests
url = 'https://api.github.com'

response = requests.get(url)

#By default it is json() formatted
print(f"The value of headers information\n{response.headers}")

#retrieving the value as a dict key/value pair
print(f"{response.headers['Content-Type']}")

#it is not case sensitive
print(f"{response.headers['content-type']}")
