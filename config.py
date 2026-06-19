import os

from dotenv import find_dotenv, load_dotenv

from pages.base_page import BasePage

load_dotenv(find_dotenv())


class UserCredentials:
    def __init__(self):
        self.email = None

    def check_password(self):
        current_test = os.environ.get("PYTEST_CURRENT_TEST", "")
        if "test_sign_up.py" not in current_test:
            if not os.getenv("PASSWORD"):
                raise ValueError("Fill password in .env file!")

    @property
    def EMAIL(self):
        self.check_password()
        if os.getenv("EMAIL"):
            return os.getenv("EMAIL")
        if not self.email:
            self.email = BasePage.email_generator()
        return self.email

    @property
    def PASSWORD(self):
        self.check_password()
        return os.getenv("PASSWORD")


UserCredentials = UserCredentials()


class PageElements:
    URL = "https://выставка-защитники-отечества-нн.рф"
    EMAIL_FIELD = '[name="email"]'
    PASSWORD_FIELD = '[name="password"]'
    SIGN_UP_BUTTON = '[type="submit"]'
    EXISTING_EMAIL_NOTIFICATION = "Этот email уже зарегистрирован"
    LOG_IN_BUTTON_LOCATOR = ".btn-primary"
    CARD = ".card"
