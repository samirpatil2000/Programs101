from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH='/usr/local/bin/geckodriver'
driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)


cookie=driver.find_element_by_id("bigCookie")
cookie_count=driver.find_element_by_id("cookies")

items=[driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]


actions=ActionChains(driver)
actions.click(cookie)


for i in range(5000):
    actions.perform()
    count=cookie_count.text
