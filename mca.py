from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.mca.gov.in/content/mca/global/en/data-and-reports/company-llp-info/incorporated-closed-month.html")
# assert "Python" in driver.title
print(By.NAME)
elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/div/div/div[2]/nav/ul[1]/li/a")

# elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/section[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/form/div[1]/select")
# elem.clear()
# elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
elem2 = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[2]/ul/button[2]")
elem2.click()



input1 = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div[2]/form/div/div[2]/input")
input1.clear()
input1.send_keys("8115887652")

checkbox = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div[4]/input")
checkbox.click()

consent = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div[5]/input")
consent.click()


input1.send_keys(Keys.RETURN)


ele4 = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div/div[3]/div[1]/div/div[2]")
ele4.click()

# # ele4.send_keys(Keys.RETURN)


# input()
# ele4.send_keys(Keys.RETURN)


time.sleep(20)
driver.close()