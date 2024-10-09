import allure
from locators.account_page_locators import ResetPassPageLocators
from page_object.base_page import BasePage


class PasswordResetPage(BasePage):

    @allure.step('Нажимаем на Восстановить пароль')
    def click_password_reset_link(self):
        # Кликаем на Восстановить пароль на странице авторизации
        self.click_element(ResetPassPageLocators.RESET_PASSWORD_LINK)

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def input_email_for_reset(self, email):
        # Вводим email в поле ввода
        self.send_keys(ResetPassPageLocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        # Кликаем на Кнопку Восстановить
        self.click_element(ResetPassPageLocators.RESET_BUTTON)

    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_show_password_icon(self):
        # Кликаем на Кнопку Показать/скрыть пароль
        self.click_element(ResetPassPageLocators.SHOW_PASSWORD_BUTTON)
