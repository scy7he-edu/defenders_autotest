import allure

from config import PageElements
from src.pages.base_page import BasePage


class SignInPage(BasePage):
    @allure.step("Отрытие страницы логина")
    def open_page(self):
        self.open_url(f"{PageElements.URL}/login")

    @allure.step("Заполнение поля e-mail")
    def fill_email(self, email: str):
        self.fill_field(PageElements.EMAIL_FIELD, email)

    @allure.step("Заполнение поля пароля")
    def fill_password(self, password: str):
        self.fill_field(PageElements.PASSWORD_FIELD, password)

    @allure.step('Нажатие кнопки "Войти"')
    def proceed_sign_in(self):
        sign_in_button = (
            self.page.get_by_role("button", name=PageElements.LOG_IN_BTN_TEXT)
            .and_(self.page.locator(PageElements.LOG_IN_BUTTON_LOCATOR))
            .and_(self.page.locator(PageElements.SIGN_UP_BUTTON))
        )
        self.check_element(sign_in_button)
        sign_in_button.click()

    @allure.step("Авторизация")
    def sign_in(self, email: str, password: str):
        self.fill_email(email)
        self.fill_password(password)
        self.proceed_sign_in()
