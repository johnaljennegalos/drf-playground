import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title" : "This is a title",
    "content" : "This is a content",
    "price" : 12.22,
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())