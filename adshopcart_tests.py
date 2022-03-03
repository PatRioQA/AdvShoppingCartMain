import adshopcart_methods as methods
import adshopcart_locators as locators
import unittest


class AdshopcartPositiveTestCases(unittest.TestCase):
         @staticmethod
         def test_main_advantage_shopping_cart():
                 methods.setUp()
                 methods.create_new_user()
                 methods.log_out()
                 methods.log_in()
                 methods.check_homepage()
                 methods.delete_account()
                 methods.log_in()
                 methods.tearDown()
