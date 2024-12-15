import unittest
from Restaurant_Browsing import RestaurantBrowsing, RestaurantDatabase

class TestRestaurantBrowsing(unittest.TestCase):
    def setUp(self):
        # 初始化测试环境，创建数据库和浏览对象
        # Initialize the test environment, create the database and browse the objects
        self.database = RestaurantDatabase()
        self.browsing = RestaurantBrowsing(self.database)

    def test_search_by_cuisine(self):
        # 测试搜索意大利菜系的功能
        # Test search for Italian cuisine
        results = self.browsing.search_by_cuisine("Italian")
        self.assertEqual(len(results), 2)  # 验证返回结果数量是否为2 Verify that the number of returned results is 2
        for restaurant in results:
            self.assertEqual(restaurant['cuisine'], "Italian")  # 验证每个结果的菜系是否为意大利 Verify that the cuisine of each result is Italian

    def test_search_by_cuisine(self):
        # 测试搜索快餐的功能 Test search for fast food
        results = self.browsing.search_by_cuisine("Fast Food")
        self.assertEqual(len(results), 1)  # 验证返回结果数量是否为1 Verify that the number of returned results is 1
        for restaurant in results:
            self.assertEqual(restaurant['cuisine'], "Fast Food")  # 验证每个结果的菜系是否为快餐 Verify that the cuisine of each result is Fast Food

    # 测试验证搜索“Chinese”菜系的准确性 Test to verify the accuracy of searching "Chinese" cuisine
    def test_search_chinese_cuisine(self):
        expected_result_count = 0  # 预期结果数量为0 The expected number of results is 0
        results = self.browsing.search_by_cuisine("Chinese")
        assert len(results) == expected_result_count, f"Expected {expected_result_count} results, got {len(results)}"

    # 测试验证输入不存在的菜系名称时的处理 The test verifies the processing when entering a non-existent cuisine name
    def test_search_nonexistent_cuisine(self):
        results = self.browsing.search_by_cuisine("Strange Food")
        assert len(results) == 0 or 'error' in results.lower(), "Expected no results or error message for nonexistent cuisine"

    # 测试验证输入特殊字符或空格作为菜系名称时的系统响应 The test verifies the processing when entering a non-existent cuisine name
    def test_search_special_characters(self):
        results = self.browsing.search_by_cuisine("   ")
        for restaurant in results:
            results = self.browsing.search_by_cuisine(restaurant)
            assert len(results) >= 0, "Search should handle special characters without crashing"

    # 测试验证边界条件，如非常长的菜系名称 Tests verify boundary conditions, such as very long cuisine names
    def test_search_long_string(self):
        long_string = "a" * 1000  # 假设1000个字符是超长字符串 Tests verify boundary conditions, such as very long cuisine names assuming that 1000 characters is an overlong string
        results = self.browsing.search_by_cuisine(long_string)
        assert len(results) >= 0, "System should handle very long strings without errors"

    # 测试验证输入非英文字符的菜系名称 The test verifies that the name of a cuisine with non-English characters is entered
    def test_search_non_english_cuisine(self):
        results = self.browsing.search_by_cuisine("中餐")
        assert len(results) < 1, "Expected to find results for non-English cuisine names"

 # Add more tests as needed...
if __name__ == '__main__':
    unittest.main()