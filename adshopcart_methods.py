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

def find_title():
    # URL of website
    url = "https://advantageonlineshopping.com/#/"

    # Opening the website
    driver.get(url)

    # Getting current URL source code
    get_title = driver.title

    # Printing the title of this URL
    print("get_title")


    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url and driver.title == get_title :
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



find_title()
setUp()
tearDown()