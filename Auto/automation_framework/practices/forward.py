from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(2)
driver.get("https://youtube.com")
time.sleep(2)

#quay lại trang trước
driver.back()
time.sleep(2)

# tiến tới
driver.forward()
time.sleep(2)

driver.quit()
