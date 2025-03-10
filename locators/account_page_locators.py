from selenium.webdriver.common.by import By


class AccountPageLocators:
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input")  # инпут емейл
    INPUT_PWD = (By.XPATH, "//label[text()='Пароль']/../input")  # инпут пароль
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")  # кнопка Профиль
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")  # кнопка история заказов
    COMPLITED_TEXT = (By.XPATH, "//p[text()='Выполнен']")  # текст заказа выполнен
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # выход
    FIRST_ORDER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')])[1]")  # первый заказ
    LAST_ORDER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')])[last()]")  # последний заказ