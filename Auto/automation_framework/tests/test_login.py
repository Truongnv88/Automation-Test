from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    sleep(10)
    username=driver.find_element(By.XPATH, "//input[@name='username']")
    password=driver.find_element(By.XPATH, "//input[@name='password']")
    username.send_keys("Admin")
    password.send_keys("admin123")
    login=driver.find_element(By.XPATH,"//button[@type='submit']").click()
    sleep(7)
    driver.quit()

