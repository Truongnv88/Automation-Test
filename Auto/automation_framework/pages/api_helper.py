import requests

class APIHelper:

    BASE_URL = "https://reqres.in/api"

    def get_user_information(self, user_id: int):
        """Hàm gọi API GET để lấy thông tin user"""
        url = f"{self.BASE_URL}/users/{user_id}"
        response = requests.get(url)
        return response

    def create_user(self, name: str, job: str):
        """Hàm gọi API POST để tạo user"""
        url = f"{self.BASE_URL}/users"
        payload = {
            "name": name,
            "job": job
        }
        response = requests.post(url, json=payload)
        return response
