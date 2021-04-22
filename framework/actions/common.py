"""Module for the most common actions

The idea is to reduce the code duplication by moving the most common
user actions here.
There's no intention to use only this level in tests.
It's better to use page objects directly in case of uncommon actions

"""

from framework.ui.pages.login_page import LoginPage
from framework.ui.elements.common import MenuButton, MainMenu
from framework.ui.pages.main_page import InventoryPage
from framework.utilities.credentials_helper import User, normal_user


def open_and_login(infra, user: User) -> InventoryPage:
    """Open login page and login using provided user

    Args:
        infra: Seleniumbase BaseCase object
        user: object of User class as provided by credentials helper

    Returns:
        Inventory page

    """
    login_page = LoginPage(infra)
    login_page.open()
    login(infra, user, login_page)
    return InventoryPage(infra)


def login(infra, user, login_page: LoginPage = None) -> None:
    """Log in using given user. Doesn't open Login Page

    Assumption:
        login page is already opened

    Args:
        infra: Seleniumbase BaseCase object
        user: object of User class as provided by credentials helper
        login_page: a Page Object of Login Page.

    Returns:
        None

    """
    if login_page is None:
        login_page = LoginPage(infra)
    login_page.login_field.write(user.login)
    login_page.password_field.write(user.password)
    login_page.login_button.click()


def open_main_menu(infra) -> MainMenu:
    """Opens main menu

    Args:
        infra: Seleniumbase BaseCase object

    Returns:
        MainMenu Page Element

    """
    MenuButton(infra).click()
    return MainMenu(infra)


def logout(infra) -> LoginPage:
    """Logs out user from current session

    Args:
        infra: Seleniumbase BaseCase object

    Returns:
        Page Object for Login page

    """
    open_main_menu(infra).logout.click()
    return LoginPage(infra)


def login_as_normal_user(infra) -> InventoryPage:
    """Logs in using standard/normal user credentials

    Args:
        infra: Seleniumbase BaseCase object

    Returns:
        Inventory page

    """
    return open_and_login(infra, normal_user)
