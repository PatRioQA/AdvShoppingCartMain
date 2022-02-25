import datetime
from selenium import webdriver
import adshopcart_locators as locators



driver = webdriver.Chrome('C:/Users/Patrich/PycharmProjects/advantage_shopping_cart/chromedriver.exe')


def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get(locators.adshopcart_url)


    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url and driver.title == "&nbsp;Advantage Shopping" :
        print(f'We are at the Advantage Shopping Cart homepage -- {driver.title}')
        print(f'We are seeing title message -- "Advantage Shopping"')
    else:
        print(f'We are not at the Advantage Shopping Cart homepage. Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
tearDown()
