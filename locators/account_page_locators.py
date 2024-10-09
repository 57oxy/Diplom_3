from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Профиль в ЛК
    PROFILE_LINK = By.XPATH, '//*[@href="/account/profile"]'
    # История заказов в ЛК
    ORDER_HISTORY = By.XPATH, '//*[@href="/account/order-history"]'
    # Кнопка Выход
    EXIT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'
    # Статус заказа в Истории заказов
    ORDER_STATUS = By.XPATH, '//p[text()="Выполнен"]'
    # Номер заказа в Личном кабинете
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'


class ResetPassPageLocators:
    # Кнопка Войти на странице авторизации
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'
    # Ссылка Восстановить пароль на странице авторизации
    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'
    # Поле ввода email
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    # Поле ввода пароля
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'
    # Кнопка Восстановить
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    # Кнопка Сохранить
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'
    # Кнопка Показать/скрыть пароль
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]'
    # Поле Пароль в статусе активно
    INPUT_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'
