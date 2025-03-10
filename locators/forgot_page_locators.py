from selenium.webdriver.common.by import By


class ForgotPwdPageLocators:
    RECOVER_PWD_BUTTON = (By.XPATH, "//a[contains(., 'Восстановить пароль')]")  # кнопка Восстановить пароль
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка Войти
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")  # кнопка ввода email
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")  # кнопка Сохранить
    PWD_FIELD = (By.XPATH, "//label[text()='Пароль']/../input")  # кнопка ввода пароля
    SHOW_PWD_BUTTON = (By.XPATH, "//div[contains(@class, 'password')]/div[contains(@class, 'input__icon')]") #кнопка показать пароль
    PWD_INPUT_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
