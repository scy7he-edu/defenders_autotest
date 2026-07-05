import allure

import config
from src.pages.base_page import BasePage


class SignUpPage(BasePage):
    @allure.step("Открытие страницы регистрации")
    def open_page(self):
        self.open_url(f"{config.PageElements.URL}/register")

    @allure.step("Заполнение поля e-mail значением: {email}")
    def fill_email(self, email: str):
        self.fill_field(config.PageElements.EMAIL_FIELD, email)

    @allure.step("Завершение регистрации")
    def sign_up_proceed(self):
        sign_up_button = self.page.locator(config.PageElements.SIGN_UP_BUTTON)
        self.check_element(sign_up_button)
        sign_up_button.click()

    @allure.step("Проверка успешной регистрации")
    def check_sign_up_succeed(self):
        sign_in_button = self.page.get_by_role(
            "link", name=config.PageElements.LOG_IN_BTN_TEXT
        ).and_(self.page.locator(config.PageElements.LOG_IN_BUTTON_LOCATOR))
        self.check_element(sign_in_button)

    @allure.step("Проверка уведомления о существовании аккаунта с указанным email")
    def check_existing_email_notification(self):
        notification = self.page.locator(
            f"text={config.PageElements.EXISTING_EMAIL_NOTIFICATION}"
        )
        self.check_element(notification)
