from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://techwithtim.net")
time.sleep(10)

# button=driver.find_element_by_id("menu-item-402")
# button.click()

#<-------------------- Or You do


link=driver.find_element_by_link_text("Python Programming")
link.click()

#wait code
try:
    element=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    element.click()
    bttn=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"sow-button-19310003"))
    )
    bttn.click()
    driver.back()
    driver.back() # This for navigate to previous page
    driver.forward() # TO MOVE FORWARD
except:
    driver.close()

time.sleep(20)
driver.close()
