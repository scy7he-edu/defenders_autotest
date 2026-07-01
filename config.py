import os
import logging

from dotenv import find_dotenv, load_dotenv

from pages.base_page import BasePage


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())


class UserCredentials:
    def __init__(self):
        self._email = None
        self._password = None

    def check_password(self):
        current_test = os.environ.get("PYTEST_CURRENT_TEST", "")
        if "test_sign_up" not in current_test:
            pwd = os.getenv("PASSWORD")
            if not pwd or "here" in pwd:
                logger.error("PASSWORD is not set in .env file or is invalid!")
                raise ValueError("Fill password in .env file!")

    @property
    def EMAIL(self):
        if self._email:
            return self._email

        self.check_password()
        email = os.getenv("EMAIL")
        if email and "@" in email and "here" not in email:
            logger.info(f"Получен EMAIL из .env: {email}")
            self._email = email
        else:
            self._email = BasePage.email_generator()
            logger.info(
                f"EMAIL в .env отсутствует или невалиден. Сгенерирован динамический EMAIL: {self._email}"
            )
        return self._email

    @property
    def PASSWORD(self):
        if self._password:
            return self._password

        self.check_password()
        self._password = os.getenv("PASSWORD")
        logger.info("Получен PASSWORD из .env")
        return self._password


UserCredentials = UserCredentials()


class PageElements:
    URL = "https://выставка-защитники-отечества-нн.рф"
    EMAIL_FIELD = '[name="email"]'
    PASSWORD_FIELD = '[name="password"]'
    SIGN_UP_BUTTON = '[type="submit"]'
    EXISTING_EMAIL_NOTIFICATION = "Этот email уже зарегистрирован"
    LOG_IN_BUTTON_LOCATOR = ".btn-primary"
    CARD = ".card"
    LOG_IN_BTN_TEXT = "Войти"
