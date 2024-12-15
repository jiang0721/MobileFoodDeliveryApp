import unittest
from Order_Placement import Cart, OrderPlacement, UserProfile, RestaurantMenu
class TestOrderPlacement(unittest.TestCase):
    def setUp(self):
        self.restaurant_menu = RestaurantMenu(available_items=["Burger", "Pizza", "Salad"])
        self.user_profile = UserProfile(delivery_address="123 Main St")
        self.cart = Cart()
        self.order = OrderPlacement(self.cart, self.user_profile, self.restaurant_menu)
    def test_add_item_to_cart(self):
        message = self.cart.add_item("Burger", 8.99, 2)
        self.assertEqual(message, "Added Burger to cart")
        self.assertEqual(len(self.cart.items), 1)
    def test_validate_order_with_unavailable_item(self):
        self.cart.add_item("Pasta", 12.99, 1) # Pasta is not in the available_items list
        result = self.order.validate_order()
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Pasta is not available")

    def test_update_item_quantity_in_cart(self):
        # 测试更新购物车中项目数量的功能
        # 向购物车中添加一个名为 "Pizza" 的项目，价格为 15.99，数量为 1
        # Test the ability to update the number of items in your cart
        # Add an item called "Pizza" to your cart for 15.99 and quantity 1
        self.cart.add_item("Pizza", 15.99, 1)
        # 更新购物车中 "Pizza" 的数量为 3
        # Update the number of "pizzas" in cart to 3
        self.cart.update_item_quantity("Pizza", 3)
        # 获取购物车中的第一个项目（假设只有一个项目）
        # Get the first item in the cart (assuming there is only one item)
        item = self.cart.items[0]
        # 断言项目的名称是 "Pizza" The name of the assert project is "Pizza"
        self.assertEqual(item.name, "Pizza")
        # 断言项目的数量是 3 Assert that the number of items is 3
        self.assertEqual(item.quantity, 3)
        # 断言项目的总价是 47.97 (15.99 * 3) Assert that the total price of the item is 47.97 (15.99 * 3)
        self.assertEqual(item.get_subtotal(), 47.97)
        self.assertFalse(item["success"])
        self.assertEqual(item["message"], "Pizza available")

    def test_view_cart(self):
        # 测试查看购物车内容的功能
        # 向购物车中添加一个名为"Salad"的商品，单价为6.99，数量为2
        # Test the ability to view the contents of the cart
        # Add an item called "Salad" to the cart with a unit price of 6.99 and a quantity of 2
        self.cart.add_item("Salad", 6.99, 2)
        # 获取购物车的内容
        # Get the contents of the cart
        cart_contents = self.cart.view_cart()
        # 断言购物车中商品的数量应为1
        # Asserts that the number of items in the cart should be 1
        self.assertEqual(len(cart_contents), 1)
        # 断言购物车中第一个商品的名字叫"Salad"
        # Assert that the name of the first item in the cart is "Salad"
        self.assertEqual(cart_contents[0]["name"], "Salad")
        # 断言购物车中第一个商品的数量为2
        # Asserts that the number of the first item in the cart is 2
        self.assertEqual(cart_contents[0]["quantity"], 2)
        # 断言购物车中第一个商品的小计金额为13.98（6.99 * 2）
        # Asserts that the subtotal amount of the first item in the cart is 13.98 (6.99 * 2)
        self.assertEqual(cart_contents[0]["subtotal"], 13.98)

    def test_update_item_quantity_in_cart(self):
        # 测试更新购物车中项目数量的功能
        # 向购物车中添加一个名为 "Burger" 的项目，价格为 8.99，数量为 -1
        # Test the ability to update the number of items in your cart
        # Add an item named "Burger" to your cart for 8.99 and quantity -1
        self.cart.add_item("Burger", 8.99, -1)
        # 更新购物车中 "Pizza" 的数量为 -1
        # Update the number of "pizzas" in the cart to -1
        self.cart.update_item_quantity("Burger", -1)
        # 获取购物车中的第一个项目（假设只有一个项目）
        # Get the first item in the cart (assuming there is only one item)
        item = self.cart.items[0]
        # 断言项目的名称是 "Pizza"
        # Assert that the name of the project is "Pizza"
        self.assertEqual(item.name, "Burger")
        # 断言项目的数量是 -1
        # Asserts that the number of items is -1
        self.assertEqual(item.quantity, -1)
        # 断言项目的总价是 -8.99
        # Assert the total price of the item is -8.99
        self.assertEqual(item.get_subtotal(), -8.99)

    def test_remove_item_from_cart(self):
        # 将这些物品加入到购物车里
        # Adding items to cart
        self.cart.add_item("Burger", 8.99, 2)
        self.cart.add_item("Pizza", 15.99, 1)
        # 将这些物品移出购物车里
        # Removing item from cart
        self.cart.remove_item("Burger")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Pizza")

# Add more tests as needed...
if __name__ == "__main__":
    unittest.main()
