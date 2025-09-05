from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(3)

driver.get("https://youtube.com")
time.sleep(3)
driver.close()
