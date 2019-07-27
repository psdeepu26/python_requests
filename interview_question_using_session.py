'''
Given a rest endpoint "https://httpbin.org" which has two API path i.e. "/get" and "/post". Path "/get" supports GET method where as "/post" supports POST Method.

Please make a get http call to REST endpoint and store the value of origin field/key in variable from the response. Call that variable src_ip_address

Using the payload {"ip": src_ip_address}, make a post call to REST endpoint. Parse the output and store the value of data field/key from the POST response. If this data key is of type dict, print the value of ip else convert the data field/key to type dict and then print the ip and data-type of data field/key.


NOTE: origin and data are two key in response body return by these two API's.
'''
import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter

session_adapter = HTTPAdapter(max_retries=3)
session = requests.Session()
session.mount("https://httpbin.org",session_adapter)

url = "https://httpbin.org"

#Get request
try:
    get_response = session.get(url+"/get")
    get_response.raise_for_status()
except HTTPError as httperror:
    print(f"HTTP error found - {httperror}")
except ConnectionError as ConError:
    print(f"Connection error raised - {ConError}")
except Timeout:
    print("Request to timeout")
else:
    src_ip_address = get_response.json()['origin']
    print(f"{src_ip_address}\n")

#Post request
try:
    post_response = requests.post(url+"/post",data = {"ip" : src_ip_address})
    post_response.raise_for_status()
except HTTPError as httperror:
    print(f"HTTP error found - {httperror}")
except ConnectionError as ConError:
    print(f"Connection error raised - {ConError}")
else:
    data = post_response.json()['data']
    ip = post_response.json()['form']['ip']
    print(f"\ndata - {data} and ip is {ip}")
