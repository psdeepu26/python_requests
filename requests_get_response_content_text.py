# Get requests to get the content and text

import requests
url = 'https://api.github.com'

response = requests.get(url)
#By default the content is byte format
print(f"This is the value of Content - Raw bytes information\n{response.content}")
#So we need to use text to avoid raw byte format
print(f"This is the value of text\n{response.text}")

#converting it to json() makes us to use the response like key/value pair
print(f"This is json response\n{response.json()}")
