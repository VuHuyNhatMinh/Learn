import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint)
print(get_response.text) 

# print(get_response.json())