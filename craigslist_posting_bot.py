from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
import os.path


def find(browser):
    add_images = browser.find_element_by_xpath('//input[@name="file"]')
    if add_images:
        return add_images
    else:
        return False


browser = webdriver.Chrome('/Applications/PythonBotClass/selenium_tutorial/chromedriver')

browser.get('https://post.craigslist.org/')

# Select Location
browser.find_element_by_class_name('ui-selectmenu-text').click()

browser.find_element_by_xpath('//li[@id="ui-id-28"]').click()

browser.find_element_by_xpath('//button[@name="go"]').click()


# Post Type Page
browser.find_element_by_xpath('//input[@name="id" and @value="ho"]').click()

# Category
browser.find_element_by_xpath('//input[@name="id" and @value="143"]').click()

# Main post page
title_area = browser.find_element_by_xpath('//input[@name="PostingTitle" and @id="PostingTitle"]')
title_area.send_keys('Amazing 5 bedroom lakefront home')

city = browser.find_element_by_xpath('//input[@name="GeographicArea" and @id="GeographicArea"]')
city.send_keys('Austin, TX')

postal_code = browser.find_element_by_xpath('//input[@name="postal" and @id="postal_code"]')

postal_code.send_keys(74324)
time.sleep(1)

# main text section
main_text = browser.find_element_by_xpath('//textarea[@name="PostingBody" and @id="PostingBody"]')
main_text.send_keys('Check out a video presentation of the property: https://youtu.be/Cnvft2EaY')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys('This is a wonderful family home. Located 2 blocks from brand new High School, and 5 miles from Boysen State Park and Reservoir and Wind River Canyon (both have camping and fishing), this is a great place to live for a family of any age.')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys("$450,000")
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys('1000 ft on highway')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys("Please inquire at 307-800-1769")

# Price
price = browser.find_element_by_xpath('//input[@name="price"]')
price.send_keys(450_000)

sqft = browser.find_element_by_xpath('//input[@name="Sqft"]')
sqft.send_keys(6_200)

house_type = browser.find_element_by_xpath('//span[@id="ui-id-1-button"]').click()

actions = ActionChains(browser)

for x in range(4):
    actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER).click()
actions.perform()


laundry = browser.find_element_by_xpath('//span[@id="ui-id-2-button"]').click()
browser.find_element_by_xpath('//li[@id="ui-id-24"]').click()

bedrooms = browser.find_element_by_xpath('//span[@id="Bedrooms-button"]').click()
browser.find_element_by_xpath('//li[@id="ui-id-28"]').click()

bathrooms = browser.find_element_by_xpath('//span[@id="ui-id-4-button"]').click()
browser.find_element_by_xpath('//li[@id="ui-id-40"]').click()

email = browser.find_element_by_xpath('//input[@name="FromEMail"]')
email.send_keys('test@gmail.com')

browser.find_element_by_xpath('//button[@name="go" and @value="continue"]').click()

# Find Location
street = browser.find_element_by_xpath('//input[@name="xstreet0" and @id="xstreet0"]')
street.send_keys('4104 Shimmering Cv')
city_location = browser.find_element_by_xpath('//input[@name="city" and @id="city"]')
city_location.send_keys('Austin')

find_location = browser.find_element_by_xpath('//button[@id="search_button"]').click()
time.sleep(1)

location_submit = browser.find_element_by_xpath('//button[@class="continue bigbutton"]').click()

# Send Pictures
browser.find_element_by_xpath('//a[@id="classic"]').click()

add_images = browser.find_element_by_xpath('//input[@name="file"]')

img = []
path = '/Applications/PythonBotClass/selenium_tutorial/random_house/'
valid_image = ['.jpg', '.gif', '.png', '.tga']
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_image:
        continue
    print(f)
    img.append(f'/random_house/{f}')

for i in sorted(img):
    if add_images != False:
        print(os.getcwd() + i)
        add_images.send_keys(os.getcwd() + i)
        add_images = WebDriverWait(browser, 3).until(find)
    else:
        continue

browser.find_element_by_xpath('//button[@value="Done with Images"]').click()
