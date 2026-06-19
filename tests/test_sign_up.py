import allure
from playwright.sync_api import Page

from pages.sign_up_page import SignUpPage


@allure.feature("Регистрация")
@allure.story("Успешное создание аккаунта")
def test_sign_up(page: Page):
    sign_up_page = SignUpPage(page)
    sign_up_page.open_page()
    sign_up_page.fill_email()
    sign_up_page.sign_up_proceed()
    sign_up_page.check_sign_up_succeed()
