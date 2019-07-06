'''
Using HTTPAdapter as I need to retry the connection atleast twice/n number of times before error handeling it
Using HTTPError for catching any HTTP Errors
Using ConnectionError for catching any connection Errors
Using getpass to get the password in a secure way
'''

#Importing the required libraries
import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.adapters import HTTPAdapter
from getpass import getpass

#Defining variables
url = "https://api.github.com/search/repositories"
username = input("Enter Username: ")

#create a HTTPAdapter (Transport Adapter) for the retries
github_adapter = HTTPAdapter(max_retries=2)

#Create a session to put persistency across retries/requests
#Don't need to pass password everytime
with requests.Session() as session:
    session.auth = (username, getpass())

#Mounting the session with required parameters before requesting GET
session.mount(url,github_adapter)

try:
    #GET request to the site
    response = session.get(
        url=url,
        params={ 'q' : 'requests+language:python'},
        headers={'Accept' : 'application/vnd.github.v3.text-match+json'},
    )
    #Raising for any exceptions
    response.raise_for_status()
except HTTPError as httperror:
    print(f"HTTP Error found {httperror}")
except ConnectionError as ce:
    print("Connection error found {}".format(ce))
except Exception as error:
    print(f"Errors found {error}")
else:
    response = response.json()
    repository = response['items'][0]
    print(f'\nRepository name: {repository["text_matches"]}')  # Python 3.6+
    print(f'\nRepository description: {repository["description"]}')

#POST request example with data
try:
    #POST request to site
    response = session.post(
        url="http://httpbin.org/post",
        data = {"key" : "value"}
    )
    response.raise_for_status()
except Exception as error:
    print(f"Error found {error}")
else:
    response = response.json()
    print(f"\n\nResponse of POST is {response}")
