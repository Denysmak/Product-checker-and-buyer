from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


import time


#position = input("What's the position you are looking for?")
#place = input('City?')
#number_of_leads = int(input('How many leads do you need?'))

position = 'Software engineer'
place = 'New york'
number_of_leads = 100

profile = webdriver.FirefoxProfile()



firefox_options = Options()
#firefox_options.add_argument('--headless')

browser = webdriver.Firefox(options=firefox_options)

original_url = "https://www.indeed.com/?hl=en&co=us&countrySelector=1"
browser.get(original_url)
time.sleep(3)

position_input = browser.find_element(By.ID, 'text-input-what')
place_input = browser.find_element(By.ID, 'text-input-where')

position_input.clear()
position_input.send_keys(position)
place_input.clear()
place_input.send_keys(place)

place_input.send_keys(Keys.RETURN)




