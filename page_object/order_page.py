import allure
from locators.order_page_locators import OrderPageLocators
from page_object.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        # Кликаем на Ссылку на заказ в Ленте заказов
        self.click_element(OrderPageLocators.ORDER_LINK)

    @allure.step('Ищем заказ по номеру в Ленте заказов')
    def get_order_in_list(self, order):
        # Записываем положение заказа
        locator = OrderPageLocators.ORDER_NUMBER_IN_LIST
        # Корректируем форматирование заказа
        locator = locator.format(order)
        # Возвращаем список заказов
        return self.get_element_text(locator)

    @allure.step('Получаем общее количество заказов, выполненных за все время')
    def get_alltime_orders_total(self):
        # Возвращаем текст элемента Количество выполненных заказов (за все время)
        return self.get_element_text(OrderPageLocators.ORDERS_TOTAL)

    @allure.step('Получаем общее количество заказов, выполненных за сегодня')
    def get_today_orders_total(self):
        # Возвращаем текст Количество выполненных заказов (за сегодня)
        return self.get_element_text(OrderPageLocators.ORDERS_TODAY)

    @allure.step('Ищем заказ по номеру среди заказов в работе')
    def get_order_number_in_work(self):
        # Возвращаем текст Номера заказов в работе
        return self.get_element_text(OrderPageLocators.ORDER_IN_WORK)
