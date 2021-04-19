from framework.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.saucedemo.com/'
    USER_NAME_ENTRY = '#user-name'
    PASSWORD_ENTRY = '#password'
    SUBMIT_BUTTON = 'input[type="submit"]'
    LOGIN_BUTTON = '#login-button'
    LOGIN_ERROR_BUTTON = 'button.error-button'
    LOGIN_ERROR_TEXT = 'h3[data-test="error"]'

    def __init__(self, infra):
        """Page Object class for Login Page

        :param infra: infrastructure described in BaseCase class
        """
        super().__init__(infra)

    @property
    def login_field(self):
        return self.do.wait_for_element_visible(self.USER_NAME_ENTRY)

    @property
    def password_field(self):
        return self.do.wait_for_element_visible(self.PASSWORD_ENTRY)

    @property
    def login_button(self):
        return self.do.wait_for_element_visible(self.LOGIN_BUTTON)

    def type_login(self, text):
        self.do.type(self.USER_NAME_ENTRY, text)

    def type_password(self, text):
        self.do.type(self.PASSWORD_ENTRY, text)

    def submit(self):
        self.do.click(self.LOGIN_BUTTON)
