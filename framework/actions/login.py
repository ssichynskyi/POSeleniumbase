from framework.ui.pages.login_page import LoginPage


def open_and_login(infra, user):
    login_page = LoginPage(infra)
    login_page.open()
    login(infra, user, login_page)
    return None


def login(infra, user, login_page=None):
    if login_page is None:
        login_page = LoginPage(infra)
    login_page.type_login(user.login)
    login_page.type_password(user.password)
    login_page.submit()
