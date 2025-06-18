import requests

url = "http://localhost:5000/journal"

data = {"entry": "I am feeling great today"}

response = requests.post(url, json=data)
print(response.json)
