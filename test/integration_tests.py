import unittest
from User_Registration import UserRegistration
from Order_Placement import Cart, OrderPlacement
from Payment_Processing import PaymentProcessing
from Restaurant_Browsing import RestaurantBrowsing, RestaurantDatabase

class TestIntegration(unittest.TestCase):
    def setUp(self):
        #设置必要的组件
        self.registration= UserRegistration()
        self.database =RestaurantDatabase()
        self.browsing =RestaurantBrowsing(self.database)
        self.cart = Cart()
        self.payment =PaymentProcessing()

    def test_order_process_flow(self):
        #用户注册
        reg_result =self.registration.register(
        "user@example.com", "Password123", "Password123"
        )
        self.assertTrue(reg_result['success'])
        #用户登录（假设有登录方法）
        user_profile =self.registration.login("user@example.com", "Password123")
        #用户浏览餐厅并将商品加入购物车
        restaurants =self.browsing.search("Italian")
        self.assertGreaterEqual(len(restaurants), 1)
        menu = restaurants[0]['menu']
        self.cart.add_item(menu[0]['name'], menu[0]['price'], 1)
        #用户下订单
        order = OrderPlacement(self.cart, user_profile,menu)
        order_result =order.process_order()
        self.assertTrue(order_result['success'])
        #用户进行支付
        payment_details= {
        "card_number": "1234567812345678",
        "expiry_date": "12/25",
        "cvv": "123"
        }
        payment_result =self.payment.process_payment(
        self.cart.total_amount(), "credit_card", payment_details
        )
        self.assertEqual(str(payment_result), "Payment successful, Order confirmed")

if __name__ == '__main__':
        unittest.main()