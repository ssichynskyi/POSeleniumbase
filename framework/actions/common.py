"""Module for the most common actions

The idea is to reduce the code duplication by moving the most common
user actions here.
There's no intention to use only this level in tests.
It's better to use page objects directly in case of uncommon actions

"""

from framework.ui.pages.login_page import LoginPage
from framework.ui.elements.common import MenuButton
from framework.ui.pages.main_page import MainMenu, InventoryPage


def open_and_login(infra, user):
    """Open login page and login using provided user"""
    login_page = LoginPage(infra)
    login_page.open()
    login(infra, user, login_page)
    return InventoryPage(infra)


def login(infra, user, login_page=None):
    """Log in using given user. Assumption: login page is already opened"""
    if login_page is None:
        login_page = LoginPage(infra)
    login_page.login_field.write(user.login)
    login_page.password_field.write(user.password)
    login_page.login_button.click()


def open_main_menu(infra):
    MenuButton(infra).click()
    return MainMenu(infra)


def logout(infra):
    """Log out"""
    open_main_menu(infra).logout.click()
