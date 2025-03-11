from constants import Urls, Data
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self):
        self.driver.get(Urls.LOGIN_PAGE)

    def login(self):
        self.wait_for_element(AccountPageLocators.INPUT_PWD)
        self.fill_form(AccountPageLocators.INPUT_EMAIL, Data.LOGIN)
        self.fill_form(AccountPageLocators.INPUT_PWD, Data.PWD)
        self.find_element_and_click(AccountPageLocators.BUTTON_ENTER)
        self.check_element_is_visible(MainPageLocators.ORDER_BUTTON)