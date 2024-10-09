import allure
from conftest import *
from helpers.constants import URL


class TestMainPage:

    @allure.title('Проверка перехода в Ленту заказов через хедер')
    def test_go_to_order_list(self, driver):
        # Создаем объект класса
        main_page = MainPage(driver)
        # Вызываем функцию клика на Ленту Заказов в хэдере
        main_page.click_orders_link()
        # Записываем в переменную адрес страницы, которая открыта
        current_url = main_page.get_current_url()
        # Сравниваем адрес ссылки с ожидаемым адресом страницы Ленты заказов
        assert current_url == URL.FEED

    @allure.title('Проверка перехода в Конструктор в хедере')
    def test_go_to_constructor(self, driver):
        # Создаем объект класса
        main_page = MainPage(driver)
        # Вызываем функцию клика на Личный кабинет в хэдере
        main_page.click_account_button()
        # Вызываем функцию клика на Конструктор в хэдере
        main_page.click_constructor_button()
        # Записываем в переменную адрес текущей страницы (Конструктор)
        current_url = main_page.get_current_url()
        # Проверяем, что ссылки мы находимся на главной странице
        assert current_url == URL.BASE

    @allure.title('Проверка появления всплывающего окна при клике на ингредиент')
    def test_get_ingredient_popup(self, driver):
        # Создаем объект класса
        main_page = MainPage(driver)
        # Вызываем функцию клика на Флюоресцентная булка R2-D3
        main_page.click_ingredient()
        # Проверяем, что заголовок Детали ингредиента отображается
        assert main_page.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).is_displayed() == True

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_close_ingredient_details_window(self, driver):
        # Создаем объект класса
        main_page = MainPage(driver)
        # Вызываем функцию клика на Флюоресцентная булка R2-D3
        main_page.click_ingredient()
        # Вызываем функцию клика на Кнопку закрытия всплывающего окна
        main_page.click_close_button()
        # Ожидаем пока будет доступно окно Детали ингредиента
        main_page.wait_until_element_invisibility(10, MainPageLocators.INGREDIENT_POPUP)
        # Проверяем, что заголовок Детали ингредиента отображается
        assert main_page.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        # Создаем объект класса
        main_page = MainPage(driver)
        # Записываем в переменную начальное количество ингредиентов
        before_counter = main_page.get_counter_of_ingredients()
        # Добавляем булку в корзину
        main_page.add_bun_to_basket()
        # Записываем в переменную количество ингредиентов после добавления еще одной булки
        after_counter = main_page.get_counter_of_ingredients()
        # Проверяем, что добавилось сразу 2 булки и количество ингредиентов после добавления - больше чем было
        assert after_counter == '2' and before_counter < after_counter

    @allure.title('Проверка успешного создания заказа')
    def test_successful_order(self, driver, signin):
        # Создаем объект класса
        main_page = MainPage(driver)
        # Ищем Ингредиент Флюоресцентная булка R2-D3
        main_page.find_element(MainPageLocators.INGREDIENT_BUN)
        # Вызываем функцию добавления в корзину булки
        main_page.add_bun_to_basket()
        # Вызываем функцию добавления в корзину начинки
        main_page.add_filling_to_basket()
        # Вызываем функцию добавления в корзину соуса
        main_page.add_sauce_to_basket()
        # Ищем Кнопку Оформить заказ
        main_page.find_element(MainPageLocators.ORDER_BUTTON)
        # Вызываем функцию перехода на страницу Лента заказов
        main_page.click_orders_link()
        # Ожидаем пока появится номер заказа во всплывающем окне
        main_page.wait_until_element_visibility(10, MainPageLocators.ORDER_NUMBER)
        # Проверяем, что отображается текст Ваш заказ начали готовить во всплывающем окне
        assert main_page.find_element(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True
