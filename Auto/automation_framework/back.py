from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(2)

driver.get("https://youtube.com")
time.sleep(2)

# Quay lại trang trước (google)
driver.back()
time.sleep(2)

driver.quit()
