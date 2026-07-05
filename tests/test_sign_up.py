import allure
from playwright.sync_api import Page
import pytest

from src.pages.sign_up_page import SignUpPage
from src.utils.data_generators import DataGenerator


@allure.feature("Регистрация")
@allure.story("Успешное создание аккаунта")
@pytest.mark.positive
def test_sign_up(page: Page):
    sign_up_page = SignUpPage(page)
    sign_up_page.open_page()
    sign_up_page.fill_email(DataGenerator.generate_email())
    sign_up_page.sign_up_proceed()
    sign_up_page.check_sign_up_succeed()


@allure.feature("Регистрация")
@allure.story("Получение уведомления о существовании аккаунта с указанным email")
@pytest.mark.negative
def test_sign_up_existing_email(page: Page):
    sign_up_page = SignUpPage(page)
    email = DataGenerator.generate_email()

    sign_up_page.open_page()
    sign_up_page.fill_email(email)
    sign_up_page.sign_up_proceed()
    sign_up_page.check_sign_up_succeed()

    sign_up_page.open_page()
    sign_up_page.fill_email(email)
    sign_up_page.sign_up_proceed()

    sign_up_page.check_existing_email_notification()
