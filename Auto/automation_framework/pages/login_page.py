from selenium.webdriver.common.by import By

class LoginPage:
   def __init__(self, driver):
      self.driver = driver
   def login(self, username, password):
    self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
