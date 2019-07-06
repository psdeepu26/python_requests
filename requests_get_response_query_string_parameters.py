# Get with Query string parameters

import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q':'requests+language:python'}
)

json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')
