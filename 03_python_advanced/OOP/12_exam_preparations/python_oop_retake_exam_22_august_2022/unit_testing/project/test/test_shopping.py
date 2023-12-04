from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart('AWR', 200)

    def test_init(self):
        self.assertEqual('AWR', self.shopping_cart.shop_name)
        self.assertEqual(200, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_setter_if_shop_name_does_not_start_with_capital_letter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'awr'

        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))
        self.assertEqual(self.shopping_cart.shop_name, 'AWR')

    def test_shop_name_setter_if_shop_name_does_not_consist_only_of_letters_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'AWR1'

        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))
        self.assertEqual(self.shopping_cart.shop_name, 'AWR')

    def test_add_to_cart_if_product_price_is_bigger_than_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('Multispinner', 150)
        expected = 'Product Multispinner cost too much!'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({}, self.shopping_cart.products)

    def test_add_to_cart_if_product_price_is_equal_to_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('product', 100)
        expected = 'Product product cost too much!'
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({}, self.shopping_cart.products)

    def test_add_duplicate_product_to_cart(self):
        expected = "Multispinner product was successfully added to the cart!"

        result = self.shopping_cart.add_to_cart("Multispinner", 99)
        self.assertEqual(expected, result)
        self.assertEqual({"Multispinner": 99}, self.shopping_cart.products)

        expected = "Multispinner product was successfully added to the cart!"

        result = self.shopping_cart.add_to_cart("Multispinner", 5)
        self.assertEqual(expected, result)
        self.assertEqual({"Multispinner": 5}, self.shopping_cart.products)

    def test_add_to_cart_successfully(self):
        result = self.shopping_cart.add_to_cart('Multispinner', 99.10)

        self.assertEqual('Multispinner product was successfully added to the cart!', result)
        self.assertEqual({'Multispinner': 99.10}, self.shopping_cart.products)

    def test_remove_from_cart_if_product_does_not_exist_raises_value_error(self):
        self.shopping_cart.add_to_cart('Multispinner', 99)

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('WristMax')

        self.assertEqual('No product with name WristMax in the cart!', str(ve.exception))
        self.assertEqual({'Multispinner': 99}, self.shopping_cart.products)

    def test_remove_from_cart_successfully(self):
        self.shopping_cart.add_to_cart('Multispinner', 99)
        self.shopping_cart.add_to_cart('WristMax', 80)

        result = self.shopping_cart.remove_from_cart('Multispinner')

        self.assertEqual('Product Multispinner was successfully removed from the cart!', result)
        self.assertEqual({'WristMax': 80}, self.shopping_cart.products)

    def test_add_carts(self):
        shopping_cart1 = ShoppingCart("First", 10)
        shopping_cart2 = ShoppingCart("Second", 20)

        shopping_cart1.add_to_cart("Multispinner", 10)
        shopping_cart2.add_to_cart("WristMax", 20)

        shopping_cart3 = shopping_cart1 + shopping_cart2

        self.assertEqual("FirstSecond", shopping_cart3.shop_name)
        self.assertEqual(30, shopping_cart3.budget)
        self.assertEqual({"Multispinner": 10, "WristMax": 20}, shopping_cart3.products)
        self.assertEqual(True, isinstance(shopping_cart3, ShoppingCart))

    def test_adding_carts_failure(self):
        a = "ShoppingCart"
        expected = "'str' object has no attribute 'shop_name'"
        with self.assertRaises(AttributeError) as ae:
            self.shopping_cart.__add__(a)
        self.assertEqual(expected, str(ae.exception))

    def test_buy_products_if_total_sum_is_bigger_than_the_budget_raises_value_error(self):
        self.shopping_cart.add_to_cart('Multispinner', 99)
        self.shopping_cart.add_to_cart('WristMax', 99)
        self.shopping_cart.add_to_cart('Spinning Handle', 99)

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        expected = 'Not enough money to buy the products! Over budget with 97.00lv!'
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_successfully(self):
        self.shopping_cart.add_to_cart('Multispinner', 99)
        self.shopping_cart.add_to_cart('WristMax', 99)

        result = self.shopping_cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 198.00lv.'

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()