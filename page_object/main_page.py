import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from page_object.base_page import BasePage
from helpers.constants import *


class MainPage(BasePage):
    @allure.step('Переходим на страницу ЛК')
    def click_account_button(self):
        # Кликаем на ссылку Личный кабинет в хэдере
        self.click_element(MainPageLocators.ACCOUNT_LINK)

    @allure.step('Переходим на страницу Лента заказов')
    def click_orders_link(self):
        # Кликаем на Ленту Заказов в хэдере
        self.click_element(OrderPageLocators.ORDER_LINK)
        # Ожидаем видимость элемента Заголовок Лента заказов
        self.wait_until_element_visibility(10, OrderPageLocators.ORDER_TITLE)


    @allure.step('Переходим в Конструктор')
    def click_constructor_button(self):
        # Кликаем на Конструктор в хэдере
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)
        # Ожидаем видимость элемента Заголовок Конструктор
        self.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем на ингредиент')
    def click_ingredient(self):
        # Кликаем на ингредиент Флюоресцентная булка R2-D3
        self.click_element(MainPageLocators.INGREDIENT_BUN)
        # Ожидаем видимость элемента Заголовок всплывающего окна Детали ингредиента
        self.wait_until_element_visibility(10, MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Закрываем всплывающее окно крестиком')
    def click_close_button(self):
        # Кликаем на Кнопку закрытия всплывающего окна
        self.click_element(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def click_order_button(self):
        # Кликаем на Кнопку Оформить заказ
        self.click_element(MainPageLocators.ORDER_BUTTON)
        self.wait_until_element_visibility(10, MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Добавляем ингредиент "Флюоресцентная булка" в корзину заказа')
    def add_bun_to_basket(self):
        # Перемещаем ингредиент Флюоресцентная булка R2-D3 в корзину
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавляем ингредиент "Говяжий метеорит (отбивная)" в корзину заказа')
    def add_filling_to_basket(self):
        # Кликаем на Раздел Начинки
        self.click_element(MainPageLocators.FILLING)
        # Перемещаем ингредиент Мясо бессмертных моллюсков Protostomia в корзину
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавляем ингредиент "Соус Spicy-X" в корзину заказа')
    def add_sauce_to_basket(self):
        # Кликаем на Раздел Соусы
        self.click_element(MainPageLocators.SAUCES)
        # Перемещаем ингредиент Соус фирменный Space Sauce в корзину
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Получаем количество добавленного в корзину ингредиента')
    def get_counter_of_ingredients(self):
        # Получаем текст элемента Счетчик ингредиентов Флюоресцентная булка
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создаем заказ и получаем его номер')
    def create_order(self):
        # Открываем главную страницу сайта
        self.go_to_site(URL.BASE)
        # Ожидаем пока будет доступен Заголовок Соберите бургер
        self.wait_until_element_visibility(20, MainPageLocators.CONSTRUCTOR_TITLE)
        # Перемещаем булку в корзину
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        # Кликаем на начинки
        self.click_element(MainPageLocators.FILLING)
        # Перемещаем начинку в корзину
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        # Кликаем на соусы
        self.click_element(MainPageLocators.SAUCES)
        # Перемещаем соус в корзину
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)
        # Кликаем на Кнопку Оформить заказ
        self.click_element(MainPageLocators.ORDER_BUTTON)
        # Ожидаем пока появится текст Ваш заказ начали готовить во всплывающем окне
        self.wait_until_element_visibility(10, MainPageLocators.ORDER_STATUS_TEXT)
        # Ожидаем пока пропадет Дефолтный номер заказа во всплывающем окне
        self.wait_until_element_invisibility(20, MainPageLocators.DEFAULT_ORDER)
        # Записываем номер заказа в переменную
        order_number = self.get_element_text(MainPageLocators.ORDER_NUMBER)
        # Нажимаем кнопку закрытия всплывающего окна
        self.click_element(MainPageLocators.CLOSE_BUTTON)
        # Возвращаем номер заказа
        return order_number
