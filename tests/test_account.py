import pytest

from pages.account_page import AccountPage


class TestAccount:

    def test_redirect_by_click_account_button(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_account_page_open()


    def test_check_history(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_history_page_redirect()


    def test_log_out(self, driver, login):
        account_page = AccountPage(driver)
        account_page.log_out()