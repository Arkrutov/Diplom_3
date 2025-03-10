import allure

from locators.account_page_locators import AccountPageLocators
from locators.forgot_page_locators import ForgotPwdPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Переходим в личный кабинет')
    def check_account_page_open(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.check_element_is_visible(AccountPageLocators.PROFILE_BUTTON)

    @allure.step('Переходим в историю заказов')
    def check_history_page_redirect(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.check_element_is_visible(AccountPageLocators.COMPLITED_TEXT)

    @allure.step('Выход')
    def log_out(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.EXIT_BUTTON)
        self.check_element_is_visible(ForgotPwdPageLocators.EMAIL_FIELD)
