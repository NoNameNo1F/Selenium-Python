from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
""" DOCUMENTATIONS:
https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.switch_to
https://www.geeksforgeeks.org/find_element_by_id-driver-method-selenium-python/
https://www.selenium.dev/documentation/webdriver/elements/locators/
https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
https://www.youtube.com/watch?v=U6gbGk5WPws&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=3
[TUTORIAL#2] https://youtu.be/b5jt2bhSeXs
"""

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)


""" ================ OLD CODE ================
search_by_name = driver.find_element(By.NAME, "Py")

first we attach value to search is: "test" at the element we finding
currently is "s" 
then we press the Enter by using "Keys.RETURN"


search_by_name.send_keys("test")
search_by_name.send_keys(Keys.RETURN)



we try to catch articles from main ID 
then we go into every article that contain ID="entry-summary" and got the header 

try:
	main = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "main"))
	)

	articles = main.find_elements(By.TAG_NAME, "article")
	for article in articles:
		header = article.find_element(By.CLASS_NAME, "entry-summary")
		print(header.text)

finally:
	driver.quit()
================ OLD CODE ================ """ 

find_by_class = driver.find_element(By.PARTIAL_LINK_TEXT, "Python")
#time.sleep(2)
find_by_class.send_keys(Keys.RETURN)
#time.sleep(2)

try:
	#branch can check
	main = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "tutorials__TutorialsList-sc-179hc97-2.jWxNWw"))
	)
	# container chua cac thu muc con 
	tutorials = main.find_elements(By.CLASS_NAME, "tutorial__TutorialCardContainer-sc-1rebzxr-0.kiZnIX")
	for tutorial in tutorials:
		header = tutorial.find_element(By.CLASS_NAME, "tutorial__TutorialCardDescription-sc-1rebzxr-5.cCJBOH")
		print(header.text)
		print('\n')
finally:
	driver.quit()

# driver.quit()
