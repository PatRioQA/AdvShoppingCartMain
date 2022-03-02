import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s = Service('C:/Users/Patrich/PycharmProjects/advantage_shopping_cart/chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get(locators.adshopcart_url)

   # print(driver.title)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url and driver.title == " Advantage Shopping" :
        print(f'We are at the Advantage Shopping Cart homepage -- {driver.title}')
        print(f'We are seeing title message -- "Advantage Shopping"')
    else:
        print(f'We are not at the Advantage Shopping Cart homepage. Check your code!')
        driver.close()
        driver.quit()

def create_new_user():
    driver.find_element(By.CSS_SELECTOR, '#menuUserLink').click()
    sleep(2.5)
    driver.find_element(By.CSS_SELECTOR, ".create-new-account").click()
    sleep(0.25)
    # Enter fake data into username open field
    driver.find_element(By.CSS_SELECTOR, "[name='usernameRegisterPage']").send_keys(locators.new_username)
    sleep(0.50)
    # Click by the password open field and enter fake password
    driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']").click()
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']").send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='confirm_passwordRegisterPage']").send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='first_nameRegisterPage']").send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='last_nameRegisterPage']").send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='phone_numberRegisterPage']").send_keys(locators.phone)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='emailRegisterPage']").send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "[name='i_agree']").click()
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, '#register_btnundefined').click()
    sleep(1.25)
    driver.find_element(By.XPATH, "//*[@id='menuUserLink']").click()
    sleep(1.25)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(1.25)
    if driver.find_element(By.XPATH, "//*[@id='myAccountContainer']/div/div/div/label").is_displayed():
        print(f'New shopper {locators.first_name} {locators.last_name} is here. Test passed.')
        sleep(1.25)
    driver.find_element(By.XPATH, "//*[@id='menuUserLink']").click()
    sleep(1.25)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My orders']").click()
    sleep(1.25)


def log_out():
    driver.find_element(By.XPATH, "//*[@id='menuUserLink']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='Sign out']").click()
    sleep(2)
    if driver.current_url == locators.adshopcart_url:
        print(f'Log out successfully at: {datetime.datetime.now()}')

def log_in():
        if driver.current_url == locators.adshopcart_url:
            driver.find_element(By.XPATH, "//*[@id='menuUserLink']").click()
            sleep(1.25)
            driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(locators.new_username)
            sleep(1.25)
            driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(locators.new_password)
            sleep(1.25)
            driver.find_element(By.ID, 'sign_in_btnundefined').click()
            sleep(1.25)
            if driver.current_url == locators.adshopcart_url:
                print("Log in successfully.")

def delete_account():
    driver.find_element(By.XPATH, "//*[@id='menuUserLink']").click()
    sleep(1.25)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(1.25)
    driver.find_element(By.XPATH, "//div[text()='Delete Account']").click()
    sleep(1.25)
    driver.find_element(By.XPATH, "//div[text()='yes']").click()
    sleep(1.25)
    print('--- Check and Delete User created --- is passed')

def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
        # Make a log file with dynamic fake values
        old_instance = sys.stdout
        log_file = open('message.log', 'w')
        sys.stdout = log_file
        print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\n')
        sys.stdout = old_instance
        print("Good job lets get some jollibee")
        log_file.close()


setUp()
create_new_user()
log_out()
log_in()
delete_account()
tearDown()
