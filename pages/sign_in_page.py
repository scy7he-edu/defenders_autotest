from config import UserCredentials as UC
from config import PageElements as PE
from pages.base_page import BasePage as BC
import allure

class SignInPage(BC):

    PASSWORD_FIELD = '[name="password"]'

    def __init__(self, page):
        super().__init__(page)

    @allure.step('Отрытие страницы логина')
    def open_page(self):
        self.open_url('https://выставка-защитники-отечества-нн.рф/login')

    @allure.step('Заполнение поля e-mail')
    def fill_email(self):
        self.fill_field(PE.EMAIL_FIELD, UC.EMAIL)

    @allure.step('Заполнение поля пароля')
    def fill_password(self):
        self.fill_field(self.PASSWORD_FIELD, UC.PASSWORD)

    @allure.step('Нажатие кнопки "Войти"')
    def proceed_sign_in(self):
        sign_in_button = self.page.get_by_role('button', name="Войти").and_(self.page.locator(".btn-primary")).and_(self.page.locator('[type="submit"]'))
        self.check_element(sign_in_button)
        sign_in_button.click()