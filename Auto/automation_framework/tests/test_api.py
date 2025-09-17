import pytest
from pages.api_helper import APIHelper

class TestAPI:

    def setup_class(self):
        """Khởi tạo API helper"""
        self.api = APIHelper()

    def test_get_user_information(self):
        """Test gọi GET API và validate"""
        response = self.api.get_user_information(2)

        # Kiểm tra status code
        assert response.status_code == 200

        # Validate dữ liệu
        json_data = response.json()
        assert json_data["data"]["id"] == 2
        assert json_data["data"]["email"] == "janet.weaver@reqres.in"

    def test_create_user(self):
        """Test gọi POST API và validate"""
        response = self.api.create_user("John Doe", "QA Engineer")

        # Validate status code
        assert response.status_code == 201

        # Validate dữ liệu trả về
        json_data = response.json()
        assert json_data["name"] == "John Doe"
        assert json_data["job"] == "QA Engineer"
        assert "id" in json_data  # phải có id trả về
        assert "createdAt" in json_data
