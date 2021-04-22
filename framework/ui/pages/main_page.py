from framework.ui.pages.base_page import BasePage
from framework.ui.elements.common import MenuButton
from framework.ui.elements.shopping import ShoppingCart, OrderByButton, InventoryList, OrderByMenu


class InventoryPage(BasePage):
    URL = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, infra):
        """Main shopping site. Basic page.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)

    @property
    def inventory_list(self) -> InventoryList:
        return InventoryList(self.do)

    @property
    def main_menu_btn(self) -> MenuButton:
        return MenuButton(self.do)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return ShoppingCart(self.do)

    @property
    def order_by_button(self) -> OrderByButton:
        return OrderByButton(self.do)

    @property
    def order_by_menu(self):
        return OrderByMenu(self.do)
