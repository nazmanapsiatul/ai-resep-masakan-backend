import requests

response = requests.post(
    "http://127.0.0.1:5000/recommend",

    json={
        "bahan":"mie telur"
    }

)

print(response.json())