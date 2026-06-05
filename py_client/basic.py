import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"Query" : "Hello John"})

print(get_response.text)

print(get_response.json())