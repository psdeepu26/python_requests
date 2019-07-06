# All HTTP methods
#using https://httpbin.org/#/

import requests

#Get Method
response = requests.get(
    url = 'https://httpbin.org/get',
)
print(f"Response of GET is {response.json()}")

#Post Method
response = requests.post(
    url = 'https://httpbin.org/post',
    data = {'origin': 'src_ip_address'},
)
print(f"Response of POST is {response.json()}")

'''
requests.put('https://httpbin.org/put', data={'key':'value'})

requests.delete('https://httpbin.org/delete')

requests.head('https://httpbin.org/get')

requests.patch('https://httpbin.org/patch', data={'key':'value'})

requests.options('https://httpbin.org/get')
'''
