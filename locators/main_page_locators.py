from selenium.webdriver.common.by import By


class MainPageLocators:
    # Ссылка Личный кабинет в хэдере
    ACCOUNT_LINK = By.XPATH, '//*[@href="/account"]'
    # Ссылка Конструктор в хэдере
    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    # Ссылка Лента Заказов в хэдере
    ORDER_LINK = By.XPATH, '//p[contains(text()="Лента Заказов")]'
    # Кнопка Войти в Аккаунт
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'
    # Заголовок Соберите бургер
    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'
    # Кнопка Оформить заказ
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    # Раздел Соусы
    SAUCES = By.XPATH, '//span[text()="Соусы"]/parent::div'
    # Раздел Начинки
    FILLING = By.XPATH, '//span[text()="Начинки"]/parent::div'
    # Раздел Булки
    BREAD = By.XPATH, '//span[text()="Булки"]/parent::div'
    # Ингредиент Флюоресцентная булка R2-D3
    INGREDIENT_BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    # Ингредиент Мясо бессмертных моллюсков Protostomia
    INGREDIENT_FILLING = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]'
    # Ингредиент Соус фирменный Space Sauce
    INGREDIENT_SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'
    # Счетчик ингредиентов Флюоресцентная булка
    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]'
    # Заголовок всплывающего окна Детали ингредиента
    INGREDIENT_POPUP_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]'
    # Всплывающее окно Детали ингредиента
    INGREDIENT_POPUP = By.XPATH, '//*[contains(@class, "contentBox")]'
    # Корзина
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'
    # Номер заказа во всплывающем окне
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'
    # Дефолтный номер заказа во всплывающем окне
    DEFAULT_ORDER = By.XPATH, '//h2[text()="9999"]'
    # Ваш заказ начали готовить во всплывающем окне
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'
    # Кнопка закрытия всплывающего окна
    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
