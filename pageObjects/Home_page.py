# Defines class Login for login related web-page


# Third-party
import self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Login:
    """Defines class Login for login related web-page"""

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    user_name = "//input[@name='username']"
    password = "//input[@name='password']"
    submit = "//button[@type='submit']"
    inavlid_creds_msg = "//p[text()='Invalid credentials']"
    creds_req = "//span[text()='Required']"

    def __init__(self, driver):
        """method to initialize the class Login"""
        self.driver = driver
        self.driver.maximize_window()

    def click_url(self):
        """
        method to get url
        """

        self.driver.get(self.url)

    def click_user_name(self, username):
        """
        method to set up the username
        :param username: str: username string
        """

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.user_name))
        )
        element.send_keys(username)
        element.send_keys(Keys.ENTER)

    def click_password(self, password):
        """ "
        method to set password
        :param password:str : password string
        """

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password))
        ).send_keys(password)

    def click_login(self):
        """
        method to click login
        """

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.submit))
        ).click()

    def check_for_invalid_creds_msg(self):
        """
        method to read invalid credentials alert message
        """

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.inavlid_creds_msg)
            )
        )
        return element.is_displayed()

    def check_for_creds_required_msg(self):
        """
        method to read credentials required message
        """

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.creds_req))
        )
        return element.is_displayed()
