# Get Requests with raise_for_status()

import requests
from requests.exceptions import HTTPError

urls = ['https://api.github.com', 'https://api.github.com/invalid']

for url in urls:
    try:
        response = requests.get(url)

        # Raising an exception in case of any issues with the response get
        response.raise_for_status()

        #HTTPError is part of the requests.exception library itself
    except HTTPError as httperror:
        print("HTTP error occurred {}".format(httperror))

        #this errors are unconditional errors which will occur apart from http errors
    except Exception as error:
        print(f"Other error occurred {error}")
    else:
        print(f"Success!! for {url}")
