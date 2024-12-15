import unittest
from Payment_Processing import PaymentProcessing
from unittest.mock import patch

class TestPaymentProcessing(unittest.TestCase):
    def setUp(self):
        # 初始化PaymentProcessing类的实例，用于测试 Initialize an instance of the PaymentProcessing class for testing
        self.payment_processing = PaymentProcessing()

    def test_valid_payment(self):
        # 定义有效的支付详情
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        # 使用patch模拟支付网关的返回值 Use patch to simulate the return value of the payment gateway
        with patch.object(self.payment_processing, 'mock_payment_gateway', return_value={"status": "success"}):
            # 调用process_payment方法处理支付 Call the process payment method to process the payment
            result = self.payment_processing.process_payment({"total_amount": 100.00}, "credit_card", payment_details)
            # 断言返回结果为成功信息 The assertion returns a success message
            self.assertEqual(result, "Payment successful, Order confirmed")

    def test_invalid_payment_method(self):
        # 定义无效的支付方式和空的支付详情 Define invalid payment methods and empty payment details
        payment_details = {}
        # 调用process_payment方法处理支付 Call the process payment method to process the payment
        result = self.payment_processing.process_payment({"total_amount": 100.00}, "bitcoin", payment_details)
        # 断言返回结果包含错误信息 The assertion returns an error message
        self.assertIn("Error: Invalid payment method", result)

    def test_insufficient_funds(self):
        # 定义有效的支付详情 Define valid payment details
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        # 使用patch模拟支付网关的返回值 Use patch to simulate the return value of the payment gateway
        with patch.object(self.payment_processing, 'mock_payment_gateway',
                          return_value={"status": "failure", "message": "Insufficient funds"}):
            # 调用process_payment方法处理支付 Call the process payment method to process the payment
            result = self.payment_processing.process_payment({"total_amount": 10000.00}, "credit_card", payment_details)
            # 断言返回结果包含错误信息 The assertion returns an error message
            self.assertIn("Payment failed, please try again", result)

    def test_expired_card(self):
        # 定义有效的支付详情 Define valid payment details
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/20",  # 过期日期
            "cvv": "123"
        }
        # 使用patch模拟支付网关的返回值 Use patch to simulate the return value of the payment gateway
        with patch.object(self.payment_processing, 'mock_payment_gateway',
                          return_value={"status": "failure", "message": "Card expired"}):
            # 调用process_payment方法处理支付 Call the process payment method to process the payment
            result = self.payment_processing.process_payment({"total_amount": 100.00}, "credit_card", payment_details)
            # 断言返回结果包含错误信息 The assertion returns an error message
            self.assertIn("Payment failed, please try again", result)

    def test_invalid_card_number(self):
        # 定义有效的支付详情，但卡号无效 Define a valid payment detail, but not the card number
        payment_details = {
            "card_number": "1234",  # 无效卡号
            "expiry_date": "12/25",
            "cvv": "123"
        }
        # 使用patch模拟支付网关的返回值 Use patch to simulate the return value of the payment gateway
        with patch.object(self.payment_processing, 'mock_payment_gateway',
                          return_value={"status": "failure", "message": "Invalid card number"}):
            # 调用process_payment方法处理支付 Call the process payment method to process the payment
            result = self.payment_processing.process_payment({"total_amount": 100.00}, "credit_card", payment_details)
            # 断言返回结果包含错误信息 The assertion returns an error message
            self.assertIn("Invalid credit card details", result)

    def test_invalid_cvv(self):
        # 定义有效的支付详情，但CVV无效 Define valid payment details, but the CVV is not
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "abc"  # 无效CVV
        }
        # 使用patch模拟支付网关的返回值 Use patch to simulate the return value of the payment gateway
        with patch.object(self.payment_processing, 'mock_payment_gateway',
                          return_value={"status": "failure", "message": "Invalid CVV"}):
            # 调用process_payment方法处理支付 Call the process payment method to process the payment
            result = self.payment_processing.process_payment({"total_amount": 100.00}, "credit_card", payment_details)
            # 断言返回结果包含错误信息 The assertion returns an error message
            self.assertIn("Payment failed, please try again", result)

    # Add more tests as needed...
if __name__ == '__main__':
    unittest.main()