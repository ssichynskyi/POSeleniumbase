from framework.ui.elements.base import UIElement, Clickable, Textual, Checkable


class MenuButton(UIElement, Clickable):
    LOCATOR = '#react-burger-menu-btn'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)


class MainLogo(UIElement):
    LOCATOR = '#react-burger-menu-btn'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)


class ShoppingCart(UIElement, Clickable):
    LOCATOR = '#shopping_cart_container'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)


class FilterMenu(UIElement, Clickable):
    LOCATOR = 'div.right_component > span > select'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)
