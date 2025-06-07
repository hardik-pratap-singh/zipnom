from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")
# assert "Python" in driver.title
# print(By.NAME)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("current affairs pdf")
elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
time.sleep(10)
driver.close()