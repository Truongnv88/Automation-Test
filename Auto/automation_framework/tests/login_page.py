from selenium.webdriver.common.by import By
from base.base_test import BaseTest

class LoginPage(BaseTest):
   def login(self, username, password):
    self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username) #username
    self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
