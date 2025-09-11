from selenium import webdriver
import pytest
from time import sleep

class BaseTest:
    @pytest.fixture(scope="class", autouse= True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        sleep(5)
        request.cls.driver = self.driver
        yield #dừng
        self.driver.quit()