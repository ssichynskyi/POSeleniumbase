from pytest import mark
from seleniumbase import BaseCase
from framework.actions.common import open_and_login, logout
from framework.ui.pages.login_page import LoginPage
from framework.utilities.credentials_helper import normal_user


class Logins(BaseCase):

    def test_successful_login(self):
        page = open_and_login(self, normal_user)
        self.assertEqual(page.URL, self.get_current_url())

    def test_logout(self):
        open_and_login(self, normal_user)
        logout(self)
        self.assertEqual(LoginPage.URL, self.get_current_url())

    def test_correct_login_empty_password_and_refresh(self):
        login_page = LoginPage(self)
        login_page.open()
        self.assert_element_not_visible(login_page.LOGIN_ERROR_TEXT)
        self.assert_element_not_visible(login_page.LOGIN_ERROR_BUTTON)
        login_page.login_field.write(normal_user.login)
        login_page.login_button.click()
        self.assert_element_visible(login_page.LOGIN_ERROR_TEXT)
        self.assert_element_visible(login_page.LOGIN_ERROR_BUTTON)
        login_page.refresh()
        self.assert_element_not_visible(login_page.LOGIN_ERROR_TEXT)
        self.assert_element_not_visible(login_page.LOGIN_ERROR_BUTTON)

    def test_no_login_correct_password(self):
        login_page = LoginPage(self)
        login_page.open()
        login_page.password_field.write(normal_user.password)
        login_page.login_button.click()
        self.assert_element_visible(login_page.LOGIN_ERROR_TEXT)
        self.assert_element_visible(login_page.LOGIN_ERROR_BUTTON)
