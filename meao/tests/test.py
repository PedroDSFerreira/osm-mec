import requests

response = requests.get("http://localhost:8080/dummy/hello/Bob")
print(response.text)
