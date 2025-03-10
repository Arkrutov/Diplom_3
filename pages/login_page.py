from constants import Urls, Data
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(Urls.LOGIN_PAGE)

    def login(self):
        base_page = BasePage(self.driver)
        base_page.wait_for_element(AccountPageLocators.INPUT_PWD)
        base_page.fill_form(AccountPageLocators.INPUT_EMAIL, Data.LOGIN)
        base_page.fill_form(AccountPageLocators.INPUT_PWD, Data.PWD)
        base_page.find_element_and_click(AccountPageLocators.BUTTON_ENTER)
        base_page.check_element_is_visible(MainPageLocators.ORDER_BUTTON)