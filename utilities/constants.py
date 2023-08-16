# Standard library
import random
import string
import os
from enum import Enum


class LoginCreds:
    LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"


class PIMSTRINGS:
    EMPLOYEE_NAME = "Linda Jane Anderson"
    SCREEN_SHOTS_PATH = os.getcwd()
    FIRST_NAME = "Aima"
    MIDDLE_NAME = "Haima"
    LAST_NAME = "Baig"
    EMERGENCY_PERSON = "Mia"
    EMERGENCY_CONTACT = int(9235)
    EMERGENCY_RELATIONSHIP = "Mother"
