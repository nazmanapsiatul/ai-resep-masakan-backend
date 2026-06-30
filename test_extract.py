import requests

response = requests.post(
    "http://192.168.0.167:5000/extract",
    json={
        "text": "Saya punya ayam, cabe dan bawang"
    }
)

print(response.json())