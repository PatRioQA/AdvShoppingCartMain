
# importing webdriver from selenium
from selenium import webdriver

# Here Chrome  will be used
driver = webdriver.Chrome()

# URL of website
url = "https://advantageonlineshopping.com/#/"

# Opening the website
driver.get(url)

# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
print(get_title)