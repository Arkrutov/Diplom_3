import allure

from constants import Data
from locators.forgot_page_locators import ForgotPwdPageLocators
from pages.base_page import BasePage

class ForgotPwdPage(BasePage):

    @allure.step('Нажимаем на восстановить пароль и проверяем переход на страницу восстановления')
    def click_recovery_pwd_and_check_redirect(self):
        self.wait_for_element(ForgotPwdPageLocators.BUTTON_ENTER)
        self.scroll_to_element(ForgotPwdPageLocators.RECOVER_PWD_BUTTON)
        self.wait_for_element(ForgotPwdPageLocators.RECOVER_PWD_BUTTON)
        self.find_element_and_click(ForgotPwdPageLocators.RECOVER_PWD_BUTTON)
        self.wait_for_element(ForgotPwdPageLocators.RECOVERY_BUTTON)
        self.check_element_is_visible(ForgotPwdPageLocators.RECOVERY_BUTTON)

    @allure.step('Вводим почту и нажимаем восстановить')
    def click_fill_email_and_recover(self):
        self.wait_for_element(ForgotPwdPageLocators.EMAIL_FIELD)
        self.fill_form(ForgotPwdPageLocators.EMAIL_FIELD, Data.REG_EMAIL)
        self.find_element_and_click(ForgotPwdPageLocators.RECOVERY_BUTTON)
        self.wait_for_element(ForgotPwdPageLocators.SAVE_BUTTON)
        self.check_element_is_visible(ForgotPwdPageLocators.SAVE_BUTTON)

    @allure.step('Вводим пароль и проверяем скрытие по кнопке')
    def fill_pwd_and_check_visibility(self):
        self.fill_form(ForgotPwdPageLocators.PWD_FIELD, Data.PWD)
        self.find_element_and_click(ForgotPwdPageLocators.SHOW_PWD_BUTTON)
        self.check_element_is_visible(ForgotPwdPageLocators.PWD_INPUT_ACTIVE)
