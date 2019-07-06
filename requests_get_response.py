# Get requests with predeifed status code

import requests
url = 'https://api.github.com'

response = requests.get(url)

#By default status code from 200 to 399 are taken as treated True and any above 400 is treated error
if response:
    print("Success!!")
else:
    print("Not valid")
