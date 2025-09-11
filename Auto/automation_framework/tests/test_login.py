from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By

from base.base_test import BaseTest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")

