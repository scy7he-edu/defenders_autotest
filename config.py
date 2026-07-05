import os
import logging
from dataclasses import dataclass, field
from dotenv import load_dotenv, find_dotenv

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())


@dataclass
class UserCredentials:
    email: str = field(init=False)
    password: str = field(init=False)

    def __post_init__(self):
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")

        if not self.EMAIL:
            logger.error("EMAIL is not set in .env file")
            raise ValueError("Fill email in .env file!")

        if not self.PASSWORD:
            logger.error("PASSWORD is not set in .env file")
            raise ValueError("Fill password in .env file!")

        logger.info(
            f"User credentials loaded: EMAIL={self.EMAIL}, PASSWORD={self.PASSWORD}"
        )


UserCredentials = UserCredentials()


@dataclass(frozen=True)
class PageElements:
    URL: str = "https://выставка-защитники-отечества-нн.рф"
    EMAIL_FIELD: str = '[name="email"]'
    PASSWORD_FIELD: str = '[name="password"]'
    SIGN_UP_BUTTON: str = '[type="submit"]'
    EXISTING_EMAIL_NOTIFICATION: str = "Этот email уже зарегистрирован"
    LOG_IN_BUTTON_LOCATOR: str = ".btn-primary"
    CARD: str = ".card"
    LOG_IN_BTN_TEXT: str = "Войти"
    WRONG_CREDENTIALS_NOTIFICATION: str = "Неверный email или пароль"


PageElements = PageElements()
