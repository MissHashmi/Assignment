import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.constants import PIMSTRINGS


class PIM:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    user_name = "//input[@name='username']"
    password = "//input[@name='password']"
    submitt = "//button[@type='submit']"
    PIM = "//a[@href='/web/index.php/pim/viewPimModule']"
    add = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    employee_name = "//label[text()='Employee Name']/.//parent::div//following-sibling::div//input[@placeholder='Type for hints...']"
    employee_id = "//label[text()='Employee Id']/.//parent::div//following-sibling::div//input[@class='oxd-input oxd-input--active']"
    user_role = "//label[text()='User Role']//parent::div//following-sibling::div//div[@tabindex='0']"
    supervisor_name = "//label[text()='Supervisor Name']/.//parent::div//following-sibling::div//input[@placeholder='Type for hints...']"
    employment_status = "//label[text()='Employment Status']"
    job_title = " //label[text()='Job Title']/.///parent::div///following-sibling::div[@tabindex='0']"

    emp_user_name = "//label[text()='Username']//parent::div//following-sibling::div//input[@autocomplete='off']"
    status = "//label[text()='Status']//parent::div//following-sibling::div//div[@tabindex='0']"
    emp_password = "//label[text()='Password']/parent::div/following-sibling::div/input[@type='password']"
    employe_name = "//input[@placeholder='Type for hints...']"
    first_name = "//input[@placeholder='First Name']"
    middle_name = "//input[@placeholder='Middle Name']"
    last_name = "//input[@placeholder='Last Name']"
    save_button = "//button[text(),'Save']"

    confirm_password = "//label[text()='Confirm Password']//parent::div//following-sibling::div//input[@type='password']"
    logout = "//a[@href='/web/index.php/auth/logout']"
    save = "//div[@class='oxd-form-actions']/button[@type='submit']"
    edit_button = "//i[contains(@class, 'bi-pencil-fill')]"
    delete_icon = "//i[contains(@class, 'bi-trash')]"
    confirm_delete = "//button[contains(text(),'Yes,Delete')]"
    add_button_on_emergency_details_page = "//button[normalize-space() = 'Add']"
    emergency_tab = "//a[text()='Emergency Contacts']"
    emergency_contact_person_field = "//label[text()='Name']/following::div[1]//input[contains(@class, 'oxd-input') and contains(@class, 'oxd-input--active')]"
    emergency_contact_relationship_field = "//label[text()='Relationship']/following::div[1]//input[contains(@class, 'oxd-input') and contains(@class, 'oxd-input--active')]"
    emergency_contact_number_field = "//label[text()='Home Telephone']/following::div[1]//input[contains(@class, 'oxd-input') and contains(@class, 'oxd-input--active')]"

    def __init__(self, driver):
        """method to initialize the class PIM"""
        self.driver = driver
        self.driver.maximize_window()

    def click_url(self):
        """method to get url"""

        self.driver.get(self.url)

    def click_user_name(self):
        """
        method to set up the username
        :param username: str: username string
        """
        elem = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.user_name))
        )
        elem.send_keys("Admin")
        elem.send_keys(Keys.ENTER)

    def click_password(self):
        """ "
        method to set password
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password))
        ).send_keys("admin123")

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.submitt))
        ).click()

    def click_PIM(self):
        """method to navigate to PIM page"""
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PIM))
        ).click()

    def click_Add(self):
        """method to click the add button on PIM tab"""

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='orangehrm-header-container']/button[@type='button']",
                )
            )
        )
        if element.text == "Add":
            element.click()

    def write_first_name(self, firstname):
        """method to type the first name
        :param firstname:str : firstname"""

        element = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable((By.XPATH, self.first_name))
            )
            .send_keys(firstname)
        )

    def write_middle_name(self, middlename):
        """method to type the middle name
        :param middlename:str : middlename"""

        element = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.middle_name)
                )
            )
            .send_keys(middlename)
        )

    def write_last_name(self, lastname):
        """method to type the last name
        :param lastname:str : lastname"""

        element = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable((By.XPATH, self.last_name))
            )
            .send_keys(lastname)
        )

    def click_save(self):
        """
        method to click save button
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(((By.XPATH, self.save)))
        ).click()

    def click_edit(self):
        """ "
        method to click edit button
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.edit_button))
        ).click()

    def click_delete(self):
        """ "
        method to click delete
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.delete_icon))
        ).click()

    def click_confirm_delete(self):
        """ "
        method to confirm delete
        """

        buttons = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='orangehrm-modal-footer']/button")
            )
        )
        for button in buttons:
            if button.text == 'Yes, Delete':
                button.click()

    def add_assigned_emergency_contact(self):
        """ "
        method to click add button on emergency contact screen
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.add_button_on_emergency_details_page)
            )
        ).click()

    def click_emergency_contact(self):
        """ "
        method to click emergency contact
        """

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.emergency_tab))
        ).click()

    def write_name_of_emergency_contact(self, emergency):
        """ "
        method to write the relationship of emergency contact with the employee
        :param Relationship:str : Relationship string
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.emergency_contact_person_field)
            )
        ).send_keys(emergency)

    def write_relationship_of_emergency_contact(self, relationship):
        """ "
        method to write the relationship of emergency contact with the employee
        :param Relationship:str : Relationship string
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.emergency_contact_relationship_field)
            )
        ).send_keys(relationship)

    def write_emergency_contact_number(self, number):
        """ "
        method to set the name of emergency contact
        :param number:int :
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.emergency_contact_number_field)
            )
        ).send_keys(number)

    def find_name(self):
        """
        method supposed for assertion on the basis of element is displayed
        """

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CLASS_NAME, "employee-image")
            )
        )
        return element.is_displayed()

    def find_emergency_contact_name(self):
        """
        method supposed for assertion on the basis of element is displayed
        """

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, f"//div[text() ='{PIMSTRINGS.EMERGENCY_PERSON}']")
            )
        )
        return element.is_displayed()

    """Future Use"""
    # def click_employee_name(self, name):
    #     """method to type the name
    #     :param name:str : name"""
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, self.employe_name))).send_keys(name)
    #
    # def click_employee_id(self, id):
    #     """method to write employe id
    #     :param:id integar
    #     """
    #     element = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, self.employee_id)))
    #     element.send_keys(id)
    #
    #
    # def click_job_title(self):
    #     """method to set job title"""
    #
    #     element = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, "//label[text()='Job Title']//parent::div//following-sibling::div//div[@tabindex='0']"
    #              )))
    #     element.send_keys(Keys.ARROW_DOWN)
    #
    # def set_employment_status(self):
    #     """method to set employment status"""
    #     element = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (
    #             By.XPATH, "//label[text()='Employment Status']//parent::div//following-sibling::div//div[@tabindex='0']"
    #             )))
    #     element.send_keys(Keys.ARROW_DOWN)
    #     element.send_keys(Keys.ARROW_DOWN)
    #
    # def select_submit(self):
    #     """method to select submit"""
    #
    #     dropdown_element = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, "//label[text()='Sub Unit']/following::div[@class='oxd-select-text-input']")
    #         )
    #     )
    #     dropdown_element.send_keys(Keys.ARROW_DOWN)
    #     dropdown_element.send_keys(Keys.ARROW_DOWN)
    #     random.choice(WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(
    #         (By.XPATH, "//div[@class='oxd-select-text-input']"))))
    #
    # def click_job_title(self):
    #     """method to set the job-title button on PIM tab for searching purpose"""
    #     element = WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, "//label[text()='Job Title']//parent::div//following-sibling::div//div[@tabindex='0']"
    #              )))
    #     element.send_keys(Keys.ARROW_DOWN)
