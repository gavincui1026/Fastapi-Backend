import requests

def test_login():
    url = "http://localhost:8000/login/verification_code"
    payload = {
        "email": "",
        "verification_code": ""
    }
    response = requests.post(url, json=payload)
