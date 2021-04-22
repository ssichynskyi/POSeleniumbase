from pytest import mark
from seleniumbase import BaseCase
from framework.actions.common import login_as_normal_user


class SurfingAndBuying(BaseCase):
    """Test cases related to product surfing and buying"""

    def test_shopping_cart_icon_(self):
        main_page = login_as_normal_user(self)
        # Test index is increasing when adding items to cart
        for index in range(len(main_page.inventory_list)):
            item = main_page.inventory_list[index]
            item.add_remove_button.click()
            self.assertEqual(str(index + 1), main_page.shopping_cart.text)
        # Test index is decreasing when removing items to cart
        for index in range(len(main_page.inventory_list) - 1, 0, -1):
            item = main_page.inventory_list[index]
            item.add_remove_button.click()
            self.assertEqual(str(index), main_page.shopping_cart.text)
        # Test index is absent when no items to cart
        item = main_page.inventory_list[0]
        item.add_remove_button.click()
        self.assert_element_absent(main_page.shopping_cart.TEXT)

    def test_inventory_button(self):
        main_page = login_as_normal_user(self)
        item = main_page.inventory_list[0]
        self.assertEqual('ADD TO CART', item.add_remove_button.text)
        item.add_remove_button.click()
        self.assertEqual('REMOVE', item.add_remove_button.text)

    def test_inventory_order(self):
        main_page = login_as_normal_user(self)
        main_page.order_by_button.click()
        # Test alphabetical inventory ordering
        main_page.order_by_menu.order_az()
        for i in range(len(main_page.inventory_list) - 1):
            self.assertGreaterEqual(
                main_page.inventory_list[i+1].title.text,
                main_page.inventory_list[i].title.text
            )

        # Test reversed alphabetical inventory ordering
        main_page.order_by_button.click()
        main_page.order_by_menu.order_za()
        for i in range(len(main_page.inventory_list) - 1):
            self.assertGreaterEqual(
                main_page.inventory_list[i].title.text,
                main_page.inventory_list[i+1].title.text
            )

        # Test pricing inventory ordering
        main_page.order_by_button.click()
        main_page.order_by_menu.order_lohi()
        for i in range(len(main_page.inventory_list) - 1):
            price_next = float(main_page.inventory_list[i+1].price.text.strip('$'))
            price_cur = float(main_page.inventory_list[i].price.text.strip('$'))
            self.assertGreaterEqual(price_next, price_cur)

        # Test reversed pricing inventory ordering
        main_page.order_by_button.click()
        main_page.order_by_menu.order_hilo()
        for i in range(len(main_page.inventory_list) - 1):
            price_next = float(main_page.inventory_list[i+1].price.text.strip('$'))
            price_cur = float(main_page.inventory_list[i].price.text.strip('$'))
            self.assertGreaterEqual(price_cur, price_next)
