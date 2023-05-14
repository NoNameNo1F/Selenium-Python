from selenium import webdriver
from selenium.webdriver.common.by import By
""" DOCUMENTATIONS
https://selenium-python.readthedocs.io/
[TUTORIAL#1] https://youtu.be/Xjv1sY630Uc
"""
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")


# get the title of the website
title = driver.title
assert title == "Web form" # if it's FALSE then pop up an ERROR
"""If it's found after 2 seconds then code execution will be continued
without wait for more 8 seconds
driver.implicitly_wait(10)
"""

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
value = message.text
#print(value)
assert value == "Received!"

# for running and close this current tab immediately
#driver.close()
# for running and quitting out totally browser
driver.quit()