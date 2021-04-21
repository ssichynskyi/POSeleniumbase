from framework.ui.pages.base_page import BasePage
from framework.ui.elements.base import ButtonWithText, EditableTextField, TextLabel, ButtonWithIcon


class LoginPage(BasePage):
    URL = 'https://www.saucedemo.com/'
    LOGIN_ENTRY = '#user-name'
    PASSWORD_ENTRY = '#password'
    # SUBMIT_BUTTON = 'input[type="submit"]'
    LOGIN_BUTTON = '#login-button'
    LOGIN_ERROR_BUTTON = "button.error-button"
    LOGIN_ERROR_TEXT = 'div.error-message-container.error'

    def __init__(self, infra):
        """Page Object class for Login Page

        :param infra: infrastructure described in BaseCase class
        """
        super().__init__(infra)

    @property
    def login_field(self):
        return EditableTextField(self.do, self.LOGIN_ENTRY)

    @property
    def password_field(self):
        return EditableTextField(self.do, self.PASSWORD_ENTRY)

    @property
    def login_button(self):
        return ButtonWithText(self.do, self.LOGIN_BUTTON)

    @property
    def error_message(self):
        return TextLabel(self.do, self.LOGIN_ERROR_TEXT)

    @property
    def error_button(self):
        return ButtonWithIcon(self.do, self.LOGIN_ERROR_BUTTON)
