from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time


class RecruitmentPage(BasePage):
    VACANCIES = (By.XPATH, "//a[text()='Vacancies']")
    BUTTON_VACANCIES = (By.XPATH, "//button[contains(.,'Add')]")
    VACANCY_NAME = (By.XPATH, "//label[contains(.,'Vacancy Name')]/parent::div/following-sibling::div/input")
    JOB_TITLE_DROPDOWN = (By.XPATH, "//label[contains(.,'Job Title')]/parent::div/following-sibling::div//i[contains(@class,'oxd-select-text--arrow')]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Type description here']")
    NUMBER_OF_POSITIONS_INPUT = (By.XPATH, "//label[contains(.,'Number of Positions')]/parent::div/following-sibling::div/input")
    HIRING_MANAGER = (By.XPATH, "//label[contains(.,'Hiring Manager')]/parent::div/following-sibling::div//input[contains(@placeholder,'Type for hints')]")
    SAVE = (By.XPATH, "//button[@type='submit']")
    USERNAME_DROPDOWN = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self, locator):
        self.click(locator)
        
    def enter_text(self, locator, text):
        self.send_keys(locator, text)
        
    def select_from_dropdown(self, dropdown_locator, option_locator):
        self.click_element(dropdown_locator)
        self.click_element(option_locator)
        
        
    def click_vacancies_link(self):
        self.click_element(self.VACANCIES)
        
    
    def click_add_vacancy_button(self):
        self.click_element(self.BUTTON_VACANCIES)
        

    def set_vacancy_name(self, vacancy_name: str):
        self.enter_text(self.VACANCY_NAME, vacancy_name)
        

    def select_job_title(self, job_title: str):
            title_xpath = f"//div[@class='oxd-select-wrapper']//div[@role='listbox']//div[@role='option']//span[.='{job_title}']"
            title_locator = (By.XPATH, title_xpath)
            self.select_from_dropdown(self.JOB_TITLE_DROPDOWN, title_locator)
            
            
    def set_description(self, description: str):
        self.enter_text(self.DESCRIPTION_TEXTAREA, description)
        

    def set_number_of_positions(self, number_of_positions: int):
        self.enter_text(self.NUMBER_OF_POSITIONS_INPUT, str(number_of_positions))        
        

    def click_save(self):
        self.click_element(self.SAVE)
    

    def add_vacancy(self, vacancy_name: str, job_title: str, description: str = "", number_of_positions: int = 1):
        self.click_vacancies_link()
        self.click_add_vacancy_button()
        self.set_vacancy_name(vacancy_name)
        self.select_job_title(job_title)
        self.set_description(description)
        self.set_number_of_positions(number_of_positions)
        self.click_save()
        