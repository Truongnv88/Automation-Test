from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from datetime import datetime


class TestVacancies(BaseTest):

    def test_add_vacancy(self):
        username = "Admin"
        password = "admin123"
        vacancy_name = "Test Automation "
        job_title = "IT Manager"
        description = "Automation selenium with Python"
        number_of_positions = 3
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_recruitment()
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_vacancy(vacancy_name, job_title, description, number_of_positions)