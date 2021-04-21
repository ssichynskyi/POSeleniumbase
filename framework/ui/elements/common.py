from framework.ui.elements.base import ButtonWithIcon, UIElement
from selenium.webdriver.common.by import By


class MenuButton(ButtonWithIcon):
    LOCATOR = '#react-burger-menu-btn'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)


class MainLogo(UIElement):
    LOCATOR = '#react-burger-menu-btn'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)


class ShoppingCart(ButtonWithIcon):
    LOCATOR = '#shopping_cart_container'
    TEXT = '#shopping_cart_container > a > span.shopping_cart_badge'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)

    @property
    def text(self):
        return self.do.get_text(self.TEXT)
