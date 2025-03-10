import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Нажимаем Конструктор и проверяем редирект')
    def click_constructor_and_check_redirect(self):
        self.wait_for_element(MainPageLocators.CONSTRUCT_BUTTON)
        self.find_element_and_click(MainPageLocators.CONSTRUCT_BUTTON)
        self.check_element_is_visible(MainPageLocators.CREATE_BURGER_TEXT)

    @allure.step('Нажимаем Лента заказов и проверяем редирект')
    def click_orders_and_check_redirect(self):
        self.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.check_element_is_visible(MainPageLocators.READY_TEXT)

    @allure.step('Нажимаем на ингредиент и проверяем поп-ап')
    def click_ingredient_and_check_pop_up(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)
        self.check_element_is_visible(MainPageLocators.INGREDIENT_TEXT)

    @allure.step('Нажимаем на крестик в поп-апе и проверяем его закрытие')
    def click_pop_up_close(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)
        self.check_element_is_visible(MainPageLocators.INGREDIENT_TEXT)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.check_element_is_not_visible(MainPageLocators.INGREDIENT_TEXT)

    @allure.step('Добавляем ингредиент и проверяем каунтер')
    def add_ingredient_and_check_counter(self):
        self.wait_for_element(MainPageLocators.SAUСES_BUTTON)
        self.find_element_and_click(MainPageLocators.SAUСES_BUTTON)
        self.drag_and_drop_element(MainPageLocators.SAUСES_SPICY, MainPageLocators.CONSTRUCT_FIELD)
        counter_element = self.find_element(MainPageLocators.COUNTER)
        assert counter_element.text == "1"

    @allure.step('Оформляем заказ')
    def made_order_and_check(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        self.check_element_is_visible(MainPageLocators.ORDER_TEXT)


