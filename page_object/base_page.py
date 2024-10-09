from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url='https://stellarburgers.nomoreparties.site/'):
        return self.driver.get(url)

    def get_current_url(self):
        # Получаем текущий открытый адрес страницы
        return self.driver.current_url

    def click_element(self, locator):
        # Ожидаем доступность элемента
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        # Кликаем на элемент
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        # Ожидаем доступность элемента
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        # Ищем элемент
        return self.driver.find_element(*locator)

    def wait_until_element_visibility(self, time, locator):
        # Ожидаем видимость элемента
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_until_element_invisibility(self, time, locator):
        # Ожидаем невидимость элемента
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def get_element_text(self, locator):
        # Получаем текст элемента
        return self.driver.find_element(*locator).text

    def send_keys(self, locator, value):
        # Вводим данные в элемент (текстовое поле)
        self.driver.find_element(*locator).send_keys(value)

    def drag_and_drop_element(self, locator_from, locator_to):
        # Ожидаем видимость начального элемента
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_from))
        # Ожидаем видимость конечного элемента
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_to))
        # Записываем положение локатора начального элемента
        element_from = self.driver.find_element(*locator_from)
        # Записываем положение локатора конечного элемента
        element_to = self.driver.find_element(*locator_to)
        # Перемещаем элемент с начального положения в конечное
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()
