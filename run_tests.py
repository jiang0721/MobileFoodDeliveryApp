import unittest

if __name__== '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover('../FoodDeliveryApp-v0.8')
    testRunner =unittest.TextTestRunner()
    testRunner.run(tests)
