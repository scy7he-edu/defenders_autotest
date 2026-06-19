import allure
from playwright.sync_api import expect

import config
from pages.base_page import BasePage


class SignUpPage(BasePage):
    @allure.step("Открытие страницы регистрации")
    def open_page(self):
        self.open_url(f"{config.PageElements.URL}/register")

    @allure.step("Заполнение поля e-mail. Первичная регистрация")
    def fill_email(self):
        self.fill_field(config.PageElements.EMAIL_FIELD, BasePage.email_generator())

    @allure.step("Заполнение поля e-mail. Регистрация уже выполнена.")
    def fill_email_exists(self):
        self.fill_field(config.PageElements.EMAIL_FIELD, config.UserCredentials.EMAIL)

    @allure.step("Завершение регистрации")
    def sign_up_proceed(self):
        sign_up_button = self.page.locator(config.PageElements.SIGN_UP_BUTTON)
        self.check_element(sign_up_button)
        sign_up_button.click()

    @allure.step("Проверка успешной регистрации")
    def check_sign_up_succeed(self):
        sign_in_button = self.page.get_by_role("link", name="Войти").and_(
            self.page.locator(config.PageElements.LOG_IN_BUTTON_LOCATOR)
        )
        self.check_element(sign_in_button)
