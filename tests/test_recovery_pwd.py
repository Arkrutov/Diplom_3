import pytest

from constants import Urls
from pages.base_page import BasePage
from pages.forgot_pwd_page import ForgotPwdPage


class TestRecoveryPwd:
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_redirect_from_recovery_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.LOGIN_PAGE)
        forgot_pwd_page = ForgotPwdPage(driver)
        forgot_pwd_page.click_recovery_pwd_and_check_redirect()

    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_recovery_pwd(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.FORGOT_PWD_PAGE)
        forgot_pwd_page = ForgotPwdPage(driver)
        forgot_pwd_page.click_fill_email_and_recover()

    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_hide_pwd_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.FORGOT_PWD_PAGE)
        forgot_pwd_page = ForgotPwdPage(driver)
        forgot_pwd_page.click_fill_email_and_recover()
        forgot_pwd_page.fill_pwd_and_check_visibility()
