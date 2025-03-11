import re
import time

import allure

from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Проверяем открытие поп-апа по клику на заказ')
    def click_order_and_check_pop_up(self):
        self.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element_and_click(OrderPageLocators.ORDER_LIST)
        self.check_element_is_visible(OrderPageLocators.STRUCTURE_TEXT)


    @allure.step('Проверяем что заказ из истории заказов отображается на странице лента заказов')
    def check_order_from_history_visible_on_order_list_page(self):
        self.wait_for_element(MainPageLocators.SAUСES_BUTTON)
        self.scroll_to_element(MainPageLocators.SAUСES_SPICY)
        self.drag_and_drop_element(MainPageLocators.SAUСES_SPICY, MainPageLocators.CONSTRUCT_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCT_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(3)
        order_pop_up = self.find_element(MainPageLocators.ORDER_POP_UP)
        order_number = order_pop_up.text
        order_number_id_only = ''.join(filter(str.isdigit, order_number.split()[0]))
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.wait_for_element(AccountPageLocators.FIRST_ORDER)
        self.scroll_to_element(AccountPageLocators.LAST_ORDER)
        order_in_acc_pop_up = self.find_element(AccountPageLocators.LAST_ORDER)
        order_number_in_acc = order_in_acc_pop_up.text
        match = re.search(r'#(\d+)', order_number_in_acc)
        if match:
            order_id = match.group(1).lstrip('0')
        assert order_number_id_only == order_id
        self.scroll_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        order_locator = self.get_order_number_locator(order_id)
        self.check_element_is_visible(order_locator)

    @allure.step('Проверяем увеличение счетчика выполнено за все время')
    def check_all_orders_counter(self):
        self.wait_for_element(MainPageLocators.SAUСES_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        order_for_all_times = self.find_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        order_for_all_times_counter = order_for_all_times.text
        self.find_element_and_click(MainPageLocators.CONSTRUCT_BUTTON)
        self.scroll_to_element(MainPageLocators.SAUСES_SPICY)
        self.drag_and_drop_element(MainPageLocators.SAUСES_SPICY, MainPageLocators.CONSTRUCT_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCT_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(3)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        order_for_all_times_after_create_order = self.find_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        order_for_all_times_after_create_order_counter = order_for_all_times_after_create_order.text
        assert order_for_all_times_counter < order_for_all_times_after_create_order_counter

    @allure.step('Проверяем увеличение счетчика выполнено за сегодня')
    def check_today_orders_counter(self):
        self.wait_for_element(MainPageLocators.SAUСES_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        today_orders = self.find_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        today_orders_counter = today_orders.text
        self.find_element_and_click(MainPageLocators.CONSTRUCT_BUTTON)
        self.scroll_to_element(MainPageLocators.SAUСES_SPICY)
        self.drag_and_drop_element(MainPageLocators.SAUСES_SPICY, MainPageLocators.CONSTRUCT_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCT_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(3)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        today_orders_after_create_order = self.find_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        today_orders_after_create_order_counter = today_orders_after_create_order.text
        assert today_orders_counter < today_orders_after_create_order_counter

    @allure.step('Проверяем наличие ордера в работе после создания заказа')
    def check_in_progress_after_create_order(self):
        self.wait_for_element(MainPageLocators.SAUСES_BUTTON)
        self.scroll_to_element(MainPageLocators.SAUСES_SPICY)
        self.drag_and_drop_element(MainPageLocators.SAUСES_SPICY, MainPageLocators.CONSTRUCT_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCT_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(3)
        order_pop_up = self.find_element(MainPageLocators.ORDER_POP_UP)
        order_number = order_pop_up.text
        order_number_id_only = ''.join(filter(str.isdigit, order_number.split()[0]))
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        order_locator = self.get_order_in_progress_locator(order_number_id_only)
        self.check_element_is_visible(order_locator)




