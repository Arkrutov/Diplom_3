from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка оформить заказ
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка личный кабинет
    CONSTRUCT_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка конструктор
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка лента заказов
    CREATE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")  # текст собери бургер
    READY_TEXT = (By.XPATH, "//p[text()='Готовы:']")  # текст собери бургер
    BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # кнопка на булку
    INGREDIENT_TEXT = (By.XPATH, "//h2[text()='Детали ингредиента']")  # кнопка на булку
    CLOSE_POP_UP_BUTTON = (By.XPATH, "(//button[contains(@class, 'close_modified')])[1]")  # крестик на поп-апе
    SAUСES_BUTTON = (By.XPATH, "//h2[text()='Соусы']")  # кнопка соусы
    SAUСES_SPICY = (By.XPATH, "//img[@alt='Соус Spicy-X']")  # Соус Spicy-X
    CONSTRUCT_FIELD = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")  # блок для создания бургера
    COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[3]") #каунтер
    ORDER_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")  # идентификатор заказа
    ORDER_POP_UP = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")  # поп-ап заказа

