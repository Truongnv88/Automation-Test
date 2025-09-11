from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from base.base_test import BaseTest as BaseTest
from login_page import LoginPage
def test_login():
    LoginPage().login("Admin", "admin123")#login

