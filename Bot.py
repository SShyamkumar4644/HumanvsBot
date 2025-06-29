import requests

url = "http://localhost:5000"
data = {
    "username": "admin",
    "password": "1234"
}

# Send POST request
response = requests.post(url, data=data)

print("Bot login status:", response.status_code)
