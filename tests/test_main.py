import pytest

from constants import Urls
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestAccount:

    def test_constructor_redirect(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.LOGIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_constructor_and_check_redirect()


    def test_orders_redirect(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.LOGIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_orders_and_check_redirect()


    def test_pop_up_ingredient_info(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient_and_check_pop_up()


    def test_close_pop_up_ingredient_info(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_pop_up_close()


    def test_check_counter_after_add_ingredient(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredient_and_check_counter()


    def test_made_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.made_order_and_check()