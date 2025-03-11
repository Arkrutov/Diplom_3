import pytest

from pages.order_page import OrderPage


class TestOrderHistory:

    def test_details_pop_up(self, driver, login):
        order_page = OrderPage(driver)
        order_page.click_order_and_check_pop_up()


    def test_order_in_history_showed_on_order_page(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_order_from_history_visible_on_order_list_page()


    def test_after_order_all_counter_grow(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_all_orders_counter()


    def test_after_order_today_counter_grow(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_today_orders_counter()


    def test_after_order_number_in_inprogres_list(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_in_progress_after_create_order()