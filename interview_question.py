'''
Given a rest endpoint "https://httpbin.org" which has two API path i.e. "/get" and "/post". Path "/get" supports GET method where as "/post" supports POST Method.

Please make a get http call to REST endpoint and store the value of origin field/key in variable from the response. Call that variable src_ip_address

Using the payload {"ip": src_ip_address}, make a post call to REST endpoint. Parse the output and store the value of data field/key from the POST response. If this data key is of type dict, print the value of ip else convert the data field/key to type dict and then print the ip and data-type of data field/key.


NOTE: origin and data are two key in response body return by these two API's.
'''


import requests

url = "https://httpbin.org"

get_response = requests.get(url+"/get")
print(f"{get_response.json()}\n")
src_ip_address = get_response.json()
print(src_ip_address['origin'])

post_response = requests.post(url+"/post", data = {"ip": src_ip_address})
post_dict_response = post_response.json()
print(post_dict_response)

post_response1 = requests.post("https://httpbin.org/post",data="this is a test")
print(f"\n\n{post_response1.json()}")
