from playwright.sync_api import Page
from pages.sign_in_page import SignInPage
import allure

@allure.feature('Авторизация')
@allure.story('Успешный вход в аккаунт')
def test_sign_in(page: Page):
    sign_in_page = SignInPage(page)
    sign_in_page.open_page()
    sign_in_page.fill_email()
    sign_in_page.fill_password()
    sign_in_page.proceed_sign_in()

    #?with allure.step('Проверка редиректа в дашборд'):
        #?expect(page).to_have_url('https://выставка-защитников-отечества-нн.рф/dashboard')