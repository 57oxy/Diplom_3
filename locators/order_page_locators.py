from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок Лента заказов
    ORDER_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    # Номер заказа в работе
    ORDER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'
    # Количество выполненных заказов (за все время)
    ORDERS_TOTAL = By.XPATH, '//p[contains(@class,"text_type_digits-large")]'
    # Количество выполненных заказов (за сегодня)
    ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'
    # Ссылка на заказ в Ленте заказов
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    # Номер заказа из Ленты заказов
    ORDER_NUMBER_IN_LIST = By.XPATH, '//p[text()="{}"]'
    # Заголовок Состав в окне с деталями заказа
    ORDER_CONTENT = By.XPATH, '//p[text()="Cостав"]'
    # Текст Все текущие заказы готовы!
    ALL_READY_TITLE = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'
