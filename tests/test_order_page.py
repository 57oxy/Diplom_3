import allure
from conftest import *
from locators.order_page_locators import OrderPageLocators
from locators.account_page_locators import AccountPageLocators
from page_object.order_page import OrderPage
from page_object.main_page import MainPage
from page_object.account_page import AccountPage


class TestOrderListPage:

    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_get_order_popup(self, driver):
        # Создаем объекты класса
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        # Вызываем функцию Перехода на страницу Лента заказов
        main_page.click_orders_link()
        # Вызываем функцию нажатия на заказ в списке Лента заказов
        order_page.click_order()
        # Проверяем, что состав в окне с деталями заказа
        assert order_page.find_element(OrderPageLocators.ORDER_CONTENT).is_displayed() == True

    @allure.title('Проверка отображения созданного заказа в Ленте заказов')
    def test_find_order_in_list(self, driver, signin):
        # Создаем объекты класса
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        account_page = AccountPage(driver)
        # Вызываем функцию создания заказа и получаем его номер
        main_page.create_order()
        # Вызываем функцию клика на Личный кабинет в хэдере
        account_page.click_account_button()
        # Вызываем функцию перехода в Историю заказов
        account_page.click_order_link()
        # Ждем, что отображается элемент Статус заказа в Истории заказов
        account_page.wait_until_element_visibility(20, AccountPageLocators.ORDER_STATUS)
        # Записываем в переменную номер заказа
        my_order = account_page.get_order_number()
        # Вызываем функцию клика на кнопку Оформить заказ
        main_page.click_orders_link()
        # Ждем, что отображается элемент Заголовок Лента заказов
        order_page.wait_until_element_visibility(15, OrderPageLocators.ORDER_TITLE)
        # Записываем в переменную список всех заказов
        order = order_page.get_order_in_list(my_order)
        # Проверяем, что заказ в списке
        assert my_order in order

    @allure.title('Проверка увеличения счетчика за все время после создания заказа')
    def test_total_orders_counter(self, driver, signin):
        # Создаем объекты класса
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        # Вызываем функцию клика на кнопку Оформить заказ
        main_page.click_orders_link()
        # Записываем в переменную список всех заказов за все время
        before_total = order_page.get_alltime_orders_total()
        # Вызываем функцию создания заказа
        main_page.create_order()
        # Вызываем функцию клика на кнопку Оформить заказ
        main_page.click_orders_link()
        # Записываем в переменную список всех заказов за все время после создания заказа
        after_total = order_page.get_alltime_orders_total()
        # Проверяем, что количество заказов изменилось в большую сторону
        assert before_total < after_total

    @allure.title('Проверка увеличения счетчика заказов за сегодня после создания заказа')
    def test_today_orders_counter(self, driver, signin):
        # Создаем объекты класса
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        # Вызываем функцию клика на кнопку Оформить заказ
        main_page.click_orders_link()
        # Записываем в переменную список всех заказов за сегодня
        start_count = order_page.get_today_orders_total()
        # Вызываем функцию создания заказа
        main_page.create_order()
        # Вызываем функцию клика на кнопку Оформить заказ
        main_page.click_orders_link()
        # Записываем в переменную список всех заказов за сегодня после создания заказа
        after_count = order_page.get_today_orders_total()
        # Проверяем, что количество заказов за сегодня изменилось в большую сторону
        assert start_count < after_count

    @allure.title('Проверка есть ли созданный заказ среди заказов в работе')
    def test_new_order_appears_in_work_list(self, driver, signin):
        # Создаем объекты класса
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        # Вызываем функцию создания заказа, записываем номер в переменную
        new_order = main_page.create_order()
        # Вызываем функцию клика на кнопку Лента заказов
        main_page.click_orders_link()
        # Ждем, что отображается элемент Все текущие заказы готовы!
        order_page.wait_until_element_invisibility(20, OrderPageLocators.ALL_READY_TITLE)
        # Вызываем функцию получения списка заказов в работе и записываем в переменную
        order_in_progress = order_page.get_order_number_in_work()
        # Проверяем, что заказ есть в списке заказов В работе
        assert new_order in order_in_progress
