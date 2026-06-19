import allure

import config
from pages.base_page import BasePage


class SignInPage(BasePage):
    @allure.step("Отрытие страницы логина")
    def open_page(self):
        self.open_url(f"{config.PageElements.URL}/login")

    @allure.step("Заполнение поля e-mail")
    def fill_email(self):
        self.fill_field(config.PageElements.EMAIL_FIELD, config.UserCredentials.EMAIL)

    @allure.step("Заполнение поля пароля")
    def fill_password(self):
        self.fill_field(
            config.PageElements.PASSWORD_FIELD, config.UserCredentials.PASSWORD
        )

    @allure.step('Нажатие кнопки "Войти"')
    def proceed_sign_in(self):
        sign_in_button = (
            self.page.get_by_role("button", name="Войти")
            .and_(self.page.locator(".btn-primary"))
            .and_(self.page.locator('[type="submit"]'))
        )
        self.check_element(sign_in_button)
        sign_in_button.click()
