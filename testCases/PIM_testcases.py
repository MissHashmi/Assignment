# standard library
import pytest

# Third-party
from selenium import webdriver

# First-party
from pageObjects.Home_page import Login
from pageObjects.PIM_page import PIM
from utilities import constants
from utilities.constants import LoginCreds, PIMSTRINGS


class TestPIM:
    username = LoginCreds.USERNAME
    password = LoginCreds.PASSWORD
    url = LoginCreds.LOGIN_URL


class Test_PIM:
    username = LoginCreds.USERNAME
    password = LoginCreds.PASSWORD
    url = LoginCreds.LOGIN_URL
    name_1 = PIMSTRINGS.EMPLOYEE_NAME
    first_name = PIMSTRINGS.FIRST_NAME
    middle_name = PIMSTRINGS.MIDDLE_NAME
    last_name = PIMSTRINGS.LAST_NAME
    emergency_person = PIMSTRINGS.EMERGENCY_PERSON
    emergency_contact = PIMSTRINGS.EMERGENCY_CONTACT
    emergency_relationship = PIMSTRINGS.EMERGENCY_RELATIONSHIP


    def test1_Add_a_new_employee_in_the_PIM_Module(self):
        """Tests the add employee functionality"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        login_object = Login(self.driver)
        login_object.click_url()
        login_object.click_user_name(self.username)
        login_object.click_password(self.password)
        login_object.click_login()
        PIM_object = PIM(self.driver)
        PIM_object.click_PIM()
        PIM_object.click_Add()
        PIM_object.write_first_name(self.first_name)
        PIM_object.write_middle_name(self.middle_name)
        PIM_object.write_last_name(self.last_name)
        PIM_object.click_save()
        self.driver.save_screenshot("screenshot.png")
        self.driver.quit()
        assert True

    def test2_EDit_exsisting_employee_in_the_PIM_Module(self):
        """Tests the edit employee functionality"""
        """This test case contains functions that are commented on using those the employes can be searched on diffrent criteria"""

        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Techwards TB-03\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
        )
        self.driver.get(self.url)
        login_object = Login(self.driver)
        login_object.click_url()
        login_object.click_user_name(self.username)
        login_object.click_password(self.password)
        login_object.click_login()
        PIM_object = PIM(self.driver)
        PIM_object.click_PIM()
        # PIM_object.click_employee_name(self.name_1)
        # PIM_object.click_employee_id(self.id)
        # PIM_object.click_job_title()
        # PIM_object.set_employment_status()
        # PIM_object.select_submit()
        PIM_object.click_edit()
        PIM_object.click_emergency_contact()
        PIM_object.add_assigned_emergency_contact()
        PIM_object.write_name_of_emergency_contact(self.emergency_person)
        PIM_object.write_relationship_of_emergency_contact(self.emergency_relationship)
        PIM_object.write_emergency_contact_number(self.emergency_contact)
        PIM_object.click_save()
        assert PIM_object.find_emergency_contact_name()
        self.driver.save_screenshot("screenshot.png")
        self.driver.quit()

    def test3_Delete_exsisting_employee_in_the_PIM_Module(self):

        """Tests the delete employee functionality"""

        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        login_object = Login(self.driver)
        login_object.click_url()
        login_object.click_user_name(self.username)
        login_object.click_password(self.password)
        login_object.click_login()
        PIM_object = PIM(self.driver)
        PIM_object.click_PIM()
        PIM_object.click_delete()
        PIM_object.click_confirm_delete()
        self.driver.save_screenshot("screenshot.png")
        self.driver.quit()
