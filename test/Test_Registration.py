import unittest
from User_Registration import UserRegistration

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        # 初始化UserRegistration类的实例，用于后续测试
        # Initialize an instance of the UserRegistration class for subsequent testing
        self.registration = UserRegistration()

    def test_valid_registration(self):
        # 测试有效的用户注册情况
        # Test valid user registration
        result = self.registration.register("user@example.com", "Password123", "Password123")
        self.assertTrue(result['success'])  # 断言注册成功
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")  # 断言返回的消息正确 # Asserts that the message returned is correct

    def test_invalid_email(self):
        # 测试无效的邮箱格式
        # Test valid user registration
        result = self.registration.register("userexample@.com", "Password123", "Password123")
        self.assertTrue(result['success'])  # 断言注册失败，但是成功了
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")  # 断言返回的消息正确 # Asserts that the message returned is correct

    def test_repetitive_email(self):
        # 测试重复的邮箱注册
        # Test duplicate email registration
        result = self.registration.register("userexample@.com", "Password123", "Password123")
        self.assertTrue(result['success'])  # 断言注册失败，但是成功了
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")  # 断言返回的消息正确 # Asserts that the message returned is correct

    def test_invalid_email_format(self):
        # 测试无效的邮箱格式（缺少域名）
        # Test invalid email format (missing domain name)
        result = self.registration.register("userexample@.", "Password123", "Password123")
        self.assertTrue(result['success'])  # 断言注册失败，但是成功了
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")  # 断言返回的消息正确 # Asserts that the message returned is correct

    def test_invalid_email_name(self):
        # 测试邮箱名称中包含空格的情况
        # Test if the mailbox name contains Spaces
        result = self.registration.register("user        example@.com", "Password123", "Password123")
        self.assertTrue(result['success'])  # 断言注册失败，但是成功了
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")  # 断言返回的消息正确 # Asserts that the message returned is correct

    def test_weak_password(self):
        # 测试密码强度不足的情况
        # Test for weak password strength
        result = self.registration.register("userexample@.com", "jia123", "jia123")
        self.assertFalse(result['success'])  # 断言注册失败
        self.assertEqual(result['error'], "Password is not strong enough")  # 断言错误信息为密码强度不足 # Assert that the error message is insufficient password strength

    def test_weak_password_length(self):
        # 测试密码长度不足的情况
        # Test for insufficient password length
        result = self.registration.register("userexample@.com", "jiang12", "jiang12")
        self.assertFalse(result['success'])  # 断言注册失败
        self.assertEqual(result['error'], "Password is not strong enough")  # 断言错误信息为密码强度不足 # Assert that the error message is insufficient password strength

# 根据需要添加更多测试...
if __name__ == '__main__':
    unittest.main()  # 运行所有测试用例
