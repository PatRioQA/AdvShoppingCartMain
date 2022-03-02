import adshopcart_methods as methods
import adshopcart_locators as locators
import unittest


class AdshopcartPositiveTestCases(unittest.TestCase):

    def test_adshopcart(self):
        setUp()
        create_new_user()
        log_out()
        log_in()
        delete_account()
        tearDown()
