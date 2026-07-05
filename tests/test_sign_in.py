import re
import allure
from playwright.sync_api import Page, expect
import pytest

from src.pages.sign_in_page import SignInPage
from config import UserCredentials, PageElements


@allure.feature("Авторизация")
@allure.story("Успешный вход в аккаунт")
def test_sign_in(page: Page):
    sign_in_page = SignInPage(page)
    sign_in_page.open_page()
    sign_in_page.sign_in(UserCredentials.EMAIL, UserCredentials.PASSWORD)

    with allure.step("Проверка редиректа в дашборд"):
        expect(page).to_have_url(re.compile(r".*/dashboard"), timeout=5000)


@allure.feature("Авторизация")
@allure.story("Вход в аккаунт с неверными данными")
@pytest.mark.negative
@pytest.mark.parametrize(
    "email, password",
    [
        ("invalid_email@example.com", "wrong_password"),
        (UserCredentials.EMAIL, "wrong_password"),
        ("invalid_email@example.com", UserCredentials.PASSWORD),
    ],
)
def test_sign_in_invalid_credentials(page: Page, email, password):
    sign_in_page = SignInPage(page)
    sign_in_page.open_page()
    sign_in_page.sign_in(email, password)

    with allure.step("Проверка уведомления о неверных данных"):
        expect(
            page.locator(f"text={PageElements.WRONG_CREDENTIALS_NOTIFICATION}")
        ).to_be_visible(timeout=5000)
