from framework.ui.elements.base import ButtonWithIcon, UIElement, ButtonWithText
from selenium.webdriver.common.by import By


class MenuButton(ButtonWithIcon):
    LOCATOR = '#react-burger-menu-btn'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        """Button that opens main menu (top left corner)

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object

        """
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)


class MainLogo(UIElement):
    LOCATOR = '.header_label'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        """Top level Website logo

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object

        """
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)


class MainMenu(UIElement):
    LOCATOR = 'div.bm-menu-wrap'
    ALL_ITEMS = '#inventory_sidebar_link'
    ABOUT = '#about_sidebar_link'
    LOGOUT = '#logout_sidebar_link'
    CLOSE = '#react-burger-cross-btn'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        """Main menu (top left corner)

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object

        """
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)

    @property
    def all_items(self):
        return ButtonWithText(self.do, self.ALL_ITEMS)

    @property
    def about(self):
        return ButtonWithText(self.do, self.ABOUT)

    @property
    def logout(self):
        return ButtonWithText(self.do, self.LOGOUT)

    @property
    def close_button(self):
        return ButtonWithIcon(self.do, self.CLOSE)
