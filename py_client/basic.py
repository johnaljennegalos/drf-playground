import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint, json={"Query" : "Hello John"})

print(get_response.text)
print(get_response.status_code)

# print(get_response.json())
# print(get_response.status_code)