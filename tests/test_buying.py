from pytest import mark
from seleniumbase import BaseCase
from framework.actions.common import open_and_login
from framework.ui.elements.common import ShoppingCart
from framework.ui.pages.main_page import InventoryList, FilterMenuButton, FilterMenu
from framework.utilities.credentials_helper import normal_user


class SurfingAndBuying(BaseCase):

    def test_shopping_cart_icon_(self):
        open_and_login(self, normal_user)
        inventory_list = InventoryList(self)
        shopping_cart = ShoppingCart(self)
        # Test index is increasing when adding new items
        for index in range(len(inventory_list)):
            item = inventory_list.get_by_index(index)
            item.add_remove_button.click()
            self.assertEqual(str(index + 1), shopping_cart.text)
        # Test index is decreasing when removing selected items
        for index in range(len(inventory_list) - 1, 0, -1):
            item = inventory_list.get_by_index(index)
            item.add_remove_button.click()
            self.assertEqual(str(index), shopping_cart.text)
        item = inventory_list.get_by_index(0)
        item.add_remove_button.click()
        self.assert_element_absent(shopping_cart.TEXT)

    def test_inventory_button(self):
        open_and_login(self, normal_user)
        item = InventoryList(self).get_by_index(0)
        self.assertEqual('ADD TO CART', item.add_remove_button.text)
        item.add_remove_button.click()
        self.assertEqual('REMOVE', item.add_remove_button.text)

    def test_inventory_order(self):
        open_and_login(self, normal_user)
        inventory_list = InventoryList(self)
        filter_menu_button = FilterMenuButton(self)
        filter_menu_button.click()
        filter_menu = FilterMenu(self)

        # Test alphabetical inventory ordering
        filter_menu.order_az()
        for i in range(len(inventory_list) - 1):
            self.assertGreaterEqual(inventory_list[i+1].title.text, inventory_list[i].title.text)

        # Test reversed alphabetical inventory ordering
        FilterMenuButton(self).click()
        filter_menu.order_za()
        for i in range(len(inventory_list) - 1):
            self.assertGreaterEqual(inventory_list[i].title.text, inventory_list[i+1].title.text)

        # Test pricing inventory ordering
        FilterMenuButton(self).click()
        filter_menu.order_lohi()
        for i in range(len(inventory_list) - 1):
            price_next = float(inventory_list[i+1].price.text.strip('$'))
            price_cur = float(inventory_list[i].price.text.strip('$'))
            self.assertGreaterEqual(price_next, price_cur)

        # Test reversed pricing inventory ordering
        FilterMenuButton(self).click()
        filter_menu.order_hilo()
        for i in range(len(inventory_list) - 1):
            price_next = float(inventory_list[i+1].price.text.strip('$'))
            price_cur = float(inventory_list[i].price.text.strip('$'))
            self.assertGreaterEqual(price_cur, price_next)
