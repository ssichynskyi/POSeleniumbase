from framework.ui.elements.base import (
    UIElement,
    ButtonWithText,
    TextLabel,
    ButtonWithIcon,
    SelectMenu,
    BaseListElement,
    BaseListOfElements
)
from selenium.webdriver.common.by import By
from framework.ui.pages.base_page import BasePage
from framework.ui.elements.common import MenuButton, ShoppingCart


class FilterMenuButton(ButtonWithIcon):
    LOCATOR = 'select.product_sort_container'

    '# header_container > div.header_secondary_container > div.right_component > span > select'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)


class FilterMenu(SelectMenu):
    LOCATOR = '.product_sort_container'
    AZ = 'az'
    ZA = 'za'
    LOHI = 'lohi'
    HILO = 'hilo'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)

    def order_az(self):
        self._select_option_by_value(self.AZ)

    def order_za(self):
        self._select_option_by_value(self.ZA)

    def order_lohi(self):
        self._select_option_by_value(self.LOHI)

    def order_hilo(self):
        self._select_option_by_value(self.HILO)


class MainMenu(UIElement):
    LOCATOR = 'div.bm-menu-wrap'
    ALL_ITEMS = '#inventory_sidebar_link'
    ABOUT = '#about_sidebar_link'
    LOGOUT = '#logout_sidebar_link'
    CLOSE = '#react-burger-cross-btn'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
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


class ProductItem(BaseListElement):
    LOCATOR = 'div.inventory_item'
    IMAGE = 'div.inventory_item_img > a > img'
    TITLE = 'div.inventory_item_description > div.inventory_item_label > a > div.inventory_item_name'
    DESCRIPTION = 'div.inventory_item_description > div.inventory_item_label > div.inventory_item_desc'
    ITEM_PRICE = 'div.inventory_item_description > div.pricebar > div.inventory_item_price'
    ADD_TO_CART_BTN = 'div.inventory_item_description > div.pricebar > button'

    def __init__(self, infra):
        """Product item in the shop.

        Is never a separate element and has no unique locators.
        Therefore everyone requires parent as a Selenium WebElement.
        This is a workaround which handles Selenium issue of
        locating elements in dynamic lists

        Args:
            infra: seleniumbase BaseCase

        """
        super().__init__(infra)
        self.image_locator = self.IMAGE
        self.add_to_cart_button_locator = self.ADD_TO_CART_BTN
        self.description_locator = self.DESCRIPTION
        self.item_price_locator = self.ITEM_PRICE
        self.title_locator = self.TITLE

    @property
    def member_locators(self) -> list:
        return [
            'image_locator',
            'add_to_cart_button_locator',
            'description_locator',
            'title_locator',
            'item_price_locator'
        ]

    @property
    def add_remove_button(self):
        return ButtonWithText(self.do, self.add_to_cart_button_locator)

    @property
    def description(self):
        return TextLabel(self.do, self.description_locator)

    @property
    def title(self):
        return TextLabel(self.do, self.title_locator)

    @property
    def price(self):
        return TextLabel(self.do, self.item_price_locator)

    @property
    def image(self):
        return UIElement(self.do, self.image_locator)


class InventoryList(BaseListOfElements):
    def __init__(self, infra):
        """List of shopping products

        Args:
            infra: Seleniumbase BaseCase

        """
        super().__init__(infra, ProductItem)

    def get_by_description(self, value):
        return self.get_by_property_value('title.text', value)


class InventoryPage(BasePage):
    URL = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, infra):
        """Main shopping site"""
        super().__init__(infra)

    @property
    def inventory_list(self):
        return InventoryList(self.do)

    @property
    def main_menu_btn(self):
        return MenuButton(self.do)

    @property
    def shopping_cart(self):
        return ShoppingCart(self.do)

    @property
    def filter_inv_button(self):
        return FilterMenuButton(self.do)
