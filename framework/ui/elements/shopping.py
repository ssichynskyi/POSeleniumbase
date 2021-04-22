"""A placeholder for all elements which are
related to product surfing and buying activities

"""

from selenium.webdriver.common.by import By
from framework.ui.elements.base import (
    ButtonWithIcon,
    BaseListElement,
    ButtonWithText,
    TextLabel,
    UIElement,
    BaseListOfElements,
    SelectMenu
)


class ShoppingCart(ButtonWithIcon):
    LOCATOR = '#shopping_cart_container'
    TEXT = '#shopping_cart_container > a > span.shopping_cart_badge'

    def __init__(self, infra, locator: str = None, by=By.CSS_SELECTOR):
        """Shopping cart button

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object
        """
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)

    @property
    def text(self):
        return self.do.get_text(self.TEXT)


class OrderByButton(ButtonWithIcon):
    LOCATOR = 'select.product_sort_container'

    '# header_container > div.header_secondary_container > div.right_component > span > select'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        """

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object
        """
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)


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
            infra: Seleniumbase BaseCase object

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
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra, ProductItem)

    def get_by_description(self, value):
        return self.get_by_property_value('title.text', value)


class OrderByMenu(SelectMenu):
    LOCATOR = '.product_sort_container'
    AZ = 'az'
    ZA = 'za'
    LOHI = 'lohi'
    HILO = 'hilo'

    def __init__(self, infra, locator=None, by=By.CSS_SELECTOR):
        """Seleniumbase BaseCase object

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object

        """
        if locator is None:
            locator = self.LOCATOR
        super().__init__(infra, locator, by)

    def order_az(self):
        """Order products by title alphabetically"""
        self._select_option_by_value(self.AZ)

    def order_za(self):
        """Order products by title in reversed alphabetical order"""
        self._select_option_by_value(self.ZA)

    def order_lohi(self):
        """Order products by price from Low to High"""
        self._select_option_by_value(self.LOHI)

    def order_hilo(self):
        """Order products by price from High to Low"""
        self._select_option_by_value(self.HILO)
