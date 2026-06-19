import allure
from playwright.sync_api import Page

from pages.sign_up_page import SignUpPage


@allure.feature('Негативный тест регистрации "аккаунт с таким email уже существует"')
@allure.story("Получение уведомления о существовании аккаунта с указанным email")
def test_sign_up_existing_email(page: Page):
    sign_up_page = SignUpPage(page)
    sign_up_page.open_page()
    sign_up_page.fill_email_exists()
    sign_up_page.sign_up_proceed()
    sign_up_page.check_existing_email_notification()
