from config import UserCredentials as UC
from config import PageElements as PE
from pages.base_page import BasePage as BC
import allure
from playwright.sync_api import expect

class SignUpPage(BC):

    SIGN_UP_BUTTON = '[type="submit"]'
    EXISTING_EMAIL_NOTIFICATION = 'Этот email уже зарегистрирован'

    def __init__(self, page):
        super().__init__(page)

    @allure.step('Открытие страницы регистрации')
    def open_page(self):
        self.open_url('https://выставка-защитники-отечества-нн.рф/register')

    @allure.step('Заполнение поля e-mail')
    def fill_email(self):
        self.fill_field(PE.EMAIL_FIELD, UC.EMAIL)

    @allure.step('Завершение регистрации')
    def sign_up_proceed(self):
        sign_up_button = self.page.locator(self.SIGN_UP_BUTTON)
        self.check_element(sign_up_button)
        sign_up_button.click()

    @allure.step('Проверка успешной регистрации')
    def check_sign_up_succeed(self):
        sign_in_button = self.page.get_by_role('link', name="Войти").and_(self.page.locator(".btn-primary"))
        self.check_element(sign_in_button)
    
    @allure.step('Проверка уведомления: email уже зарегистрирован')
    def check_existing_email_notification(self):
        notification = self.page.get_by_text(self.EXISTING_EMAIL_NOTIFICATION)
        expect(notification).to_be_visible()
        