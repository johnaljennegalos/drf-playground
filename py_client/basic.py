import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={"abc" : 123}, json={"title" : "Hello John", "content" : "This is a greeting"})

# print(get_response.text)
# print(get_response.status_code)

print(get_response.json())
# print(get_response.status_code)