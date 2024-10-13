import allure
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import HeadersLocators
from page_object.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Переходим на страницу ЛК')
    def click_account_button(self):
        # Кликаем на Личный кабинет в хэдере
        self.click_element(HeadersLocators.ACCOUNT_LINK)
        # Ожидаем когда будет доступна ссылка на Профиль пользователя
        self.wait_until_element_visibility(15, AccountPageLocators.PROFILE_LINK)

    @allure.step('Переходим в Историю заказов')
    def click_order_link(self):
        # Кликаем на Историю заказов
        self.click_element(AccountPageLocators.ORDER_HISTORY)

    @allure.step('Получаем номер заказа в Истории заказов')
    def get_order_number(self):
        # Получаем текст элемента номер заказа
        return self.get_element_text(AccountPageLocators.ORDER_NUMBER)

    @allure.step('Выходим из аккаунта по кнопке Выход в ЛК')
    def click_logout_button(self):
        # Кликаем на кнопку Выхода
        self.click_element(AccountPageLocators.EXIT_BUTTON)
