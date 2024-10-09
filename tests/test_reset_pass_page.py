import allure
from conftest import *
from helpers.constants import URL
from locators.account_page_locators import ResetPassPageLocators
from page_object.reset_pass_page import PasswordResetPage


class TestPasswordReset:
    @allure.title('Проверка перехода по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        # Создаем объект класса
        pass_reset_page = PasswordResetPage(driver)
        # Вызываем функцию перехода на главную страницу
        pass_reset_page.go_to_site(URL.LOGIN)
        # Вызываем функцию перехода на ссылку Восстановить пароль
        pass_reset_page.click_password_reset_link()
        # Смотрим адрес текущей страницы и записываем его в переменную
        current_url = pass_reset_page.get_current_url()
        # Проверяем, что мы находимся на нужной странице
        assert current_url == URL.FORGOTPASS

    @allure.title('Проверка перехода по кнопке Восстановить после ввода email')
    def test_enter_email_and_click_reset(self, driver, create_user):
        # Создаем объект класса
        pass_reset_page = PasswordResetPage(driver)
        # Вызываем функцию перехода на страницу забыли пароль
        pass_reset_page.go_to_site(URL.FORGOTPASS)
        # Вызываем функцию ввода email
        pass_reset_page.input_email_for_reset(create_user[0][0])
        # Вызываем функцию нажатия на кнопку Восстановить
        pass_reset_page.click_reset_button()
        # Ожидаем пока будет доступна кнопка Сохранить
        pass_reset_page.wait_until_element_visibility(10, ResetPassPageLocators.SAVE_BUTTON)
        # Записываем текущий адрес ссылки отображаемой страницы
        current_url = pass_reset_page.get_current_url()
        # Проверяем, что мы находимся на нужной странице
        assert current_url == URL.RESETPASS

    @allure.title('Проверка активации поля Пароль после нажатия на кнопку Показать/скрыть пароль')
    def test_show_password_input_active(self, driver, create_user):
        # Создаем объект класса
        pass_reset_page = PasswordResetPage(driver)
        # Вызываем функцию перехода на страницу забыли пароль
        pass_reset_page.go_to_site(URL.FORGOTPASS)
        # Вызываем функцию ввода email в поле для восстановления пароля
        pass_reset_page.input_email_for_reset(create_user[0][0])
        # Вызываем функцию нажатия на кнопку Восстановить
        pass_reset_page.click_reset_button()
        # Ожидаем пока будет доступна кнопка Сохранить
        pass_reset_page.wait_until_element_visibility(10, ResetPassPageLocators.SAVE_BUTTON)
        # Вызываем функцию нажатия на кнопку Показать/скрыть пароль
        pass_reset_page.click_show_password_icon()
        # Проверяем, что поле Пароль в статусе активно
        assert pass_reset_page.find_element(ResetPassPageLocators.INPUT_ACTIVE).is_displayed() == True
