import allure
from conftest import *
from locators.account_page_locators import ResetPassPageLocators
from page_object.account_page import AccountPage
from helpers.constants import URL


class TestAccountPage:

    @allure.title('Проверка перехода по кнопке Личный кабинет')
    def test_go_to_account_from_header(self, driver, signin):
        # Создаем объект класса
        account_page = AccountPage(driver)
        # Вызываем функцию клика на Личный кабинет в хэдере
        account_page.click_account_button()
        # Вызываем функцию получающую текущий адрес страницы и записываем текст страницы в переменную
        current_url = account_page.get_current_url()
        # Проверяем, что мы находимся на нужной странице профиля пользователя
        assert current_url == URL.ACCOUNT

    @allure.title('Проверка перехода в раздел История заказов')
    def test_go_to_order_history(self, driver, signin):
        # Создаем объект класса
        account_page = AccountPage(driver)
        # Вызываем функцию клика на Личный кабинет в хэдере
        account_page.click_account_button()
        # Вызываем функцию клика на Историю заказов
        account_page.click_order_link()
        # Вызываем функцию получающую текущий адрес страницы и записываем текст страницы в переменную
        current_url = account_page.get_current_url()
        # Проверяем, что мы находимся на нужной странице Списка заказов
        assert current_url == URL.ORDERS

    @allure.title('Проверка выхода из аккаунта')
    def test_user_logout(self, driver, signin):
        # Создаем объект класса
        account_page = AccountPage(driver)
        # Вызываем функцию клика на Личный кабинет в хэдере
        account_page.click_account_button()
        # Вызываем функцию клика на кнопку Выхода из аккаунта
        account_page.click_logout_button()
        # Ожидаем пока загрузится элемент Войти на странице авторизации
        account_page.wait_until_element_visibility(10, ResetPassPageLocators.ENTER_BUTTON)
        # Записываем в переменную текст элемента Войти на странице авторизации
        button_text = account_page.get_element_text(ResetPassPageLocators.ENTER_BUTTON)
        # Проверяем, что полученный текст идентичен ожидаемому
        assert button_text == 'Войти'
