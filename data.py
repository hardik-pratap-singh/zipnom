from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://www.data.gov.in/")


# def getFunc(xpath, driver):
#     s1 = driver.find_element(By.XPATH, xpath)
#     return s1



# assert "Python" in driver.title
print(By.NAME)
elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/div/div/div[2]/nav/ul[1]/li/a")
elem.send_keys(Keys.RETURN)
time.sleep(1)
# elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/section[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/form/div[1]/select")
# elem.clear()
# elem.send_keys("pycon")
elem2 = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[2]/ul/button[2]")
elem2.click()



input1 = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div[2]/form/div/div[2]/input")
# input1.clear()
input1.send_keys("8115887652")

checkbox = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div[4]/input")
checkbox.click()

consent = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div[5]/input")
consent.click()


input1.send_keys(Keys.RETURN)

time.sleep(1)
ele4 = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div/div[3]/div[1]/div/div[2]")
ele4.click()

nextbutton = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div/div[5]/button")
nextbutton.click()
# # ele4.send_keys(Keys.RETURN)
# input()
time.sleep(15)
submitButton = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div/div[6]/button")
# "/html/body/div[13]/div[2]/div[2]/div[3]/div/div/div/div/div[6]/button"
submitButton.click()
time.sleep(2)
# input()
# ele4.send_keys(Keys.RETURN)

# From here after login in the system 
# s2 = getFunc("/html/body/div[1]/div/div/div[1]/main/section[1]/div/div/div/div/form/input", driver)
searchBox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/main/section[1]/div/div/div/div/form/input")
# "/html/body/div[1]/div/div/div[1]/main/section[1]/div/div/div/div/form/input"
# # search.clear()
searchBox.send_keys("company master data")
time.sleep(1)
searchBox.send_keys(Keys.RETURN)

time.sleep(1)

anchor = driver.find_element(By.XPATH , "/html/body/div[1]/div/div/main/section[2]/div/div/div[2]/div/div[4]/div[1]/div[1]/div/div/div/div[2]/h3/a")
anchor.click()

time.sleep(1)
selectTag = driver.find_element(By.XPATH , "/html/body/div[1]/div/div/main/section[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/form/div[1]/select")
selectTag.click() 





time.sleep(240)
driver.close()