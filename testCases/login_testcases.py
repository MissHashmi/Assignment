"""Defines tests related to Login Feature"""

# Standard library
import pytest
import time
from time import sleep


# Third-party
from selenium import webdriver

# First-party
from pageObjects.Home_page import Login
from utilities.constants import LoginCreds


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Techwards TB-03\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
    )
    yield driver
    driver.quit()


class TestLogin:
    username = LoginCreds.USERNAME
    password = LoginCreds.PASSWORD
    url = LoginCreds.LOGIN_URL

    @pytest.mark.usefixtures("setup")
    def test1_homePageTitle(self, setup):
        """Tests if user is landing on the respected page"""

        driver = setup
        driver.get(self.url)
        time.sleep(5)
        act_title = driver.title
        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

    def test2_login_with_valid_credentials(self, setup):
        """Tests if user is able to log in with correct credentials"""

        driver = setup
        driver.get(self.url)
        cookies_before_login = driver.get_cookies()
        login_object = Login(setup)
        login_object.click_url()
        login_object.click_user_name(self.username)
        login_object.click_password(self.password)
        login_object.click_login()
        cookies_after_login = driver.get_cookies()
        if cookies_before_login != cookies_after_login:
            assert True
        else:
            assert False

    def test3_compare_cookies_after_login(self, setup):
        """Logs in with correct credentials and then compares the cookies before and after login"""

        driver = setup
        driver.get(self.url)
        cookies_before_login = driver.get_cookies()
        login_object = Login(setup)
        login_object.click_url()
        login_object.click_user_name(self.username)
        login_object.click_password(self.password)
        login_object.click_login()
        cookies_after_login = driver.get_cookies()
        time.sleep(5)
        if cookies_before_login != cookies_after_login:
            assert True
        else:
            assert False

    def test4_login_with_invalid_credentials(self, setup):
        """Tests if user is not allowed to log in with invalid credentials and is prompted to an error message"""

        driver = setup
        driver.get(self.url)
        cookies_before_login = driver.get_cookies()
        login_object = Login(setup)
        login_object.click_url()
        login_object.click_user_name(self.username)
        login_object.click_password("password")
        login_object.click_login()
        assert login_object.check_for_invalid_creds_msg()

    def test4_login_with_no_credentials(self, setup):
        """Tests if user is prompted to an error message when the username and password fields are blank"""

        driver = setup
        driver.get(self.url)
        login_object = Login(setup)
        login_object.click_url()
        login_object.click_login()
        time.sleep(5)
        assert login_object.check_for_creds_required_msg()
