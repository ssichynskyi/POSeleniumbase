from framework.ui.pages.base_page import BasePage
from framework.ui.elements.base import UIElement


class ProductItem(UIElement):
    # 'div.pricebar'
    LOCATOR = 'div.inventory_item'
    IMAGE = 'div.inventory_item_img'
    DESCRIPTION = 'div.inventory_item_description'
    ITEM_PRICE = 'div.inventory_item_price'
    ADD_TO_CART_BTN = 'button."btn btn_primary btn_small btn_inventory"'

    def __init__(self, infra):
        super(ProductItem, self).__init__(infra)

    def add_to_cart(self):
        self.do.click(self.ADD_TO_CART_BTN)

    def price(self):
        self.do.get_text(self.ITEM_PRICE)

    def description(self):
        self.do.get_text(self.DESCRIPTION)


class MainPage(BasePage):
    URL = 'https://www.saucedemo.com/inventory.html'
    INVENTORY = '#inventory_container'


    def __init__(self, infra):
        """Page Object class for Login Page

        :param infra: infrastructure described in BaseCase class
        """
        super().__init__(infra)

