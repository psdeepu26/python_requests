# Get requests with headers
import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={ 'q' : 'requests+language:python'},
    headers={'Accept' : 'application/vnd.github.v3.text-match+json'},
)

respository = response.json()['items'][0]
print(f"Matching repositories are {respository['text_matches']}")
