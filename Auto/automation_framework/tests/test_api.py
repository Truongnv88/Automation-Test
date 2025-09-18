import requests


def test_get_user_info():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json()
    print(data)


def test_create_user_with_token():
    login_payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    login_response = requests.post("https://reqres.in/api/login", json=login_payload)
    assert login_response.status_code == 200
    
    token = login_response.json()["token"]

    payload = {"name": "neo", "job": "chosen one"}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post("https://reqres.in/api/users", json=payload, headers=headers)
    assert response.status_code == 201
    print(response.json())
