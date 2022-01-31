from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH='/usr/local/bin/geckodriver'
driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
#driver= webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
print(driver.title)

# time.sleep(10)

search=driver.find_element_by_class_name("search-field")
search.send_keys("test") # text in search box
search.send_keys(Keys.RETURN) # Hitting enter
#print(driver.page_source) # this is for the source code
time.sleep(20)
# See in doc EXPLICIT WAIT
try:
    main=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    #print(main.text)
    time.sleep(30)
    articles=main.find_elements_by_tag_name("article")
    time.sleep(20)
    for article in articles:
        summary=article.find_element_by_class_name("entry-summary")
        print(summary.text)
        print("These are The titles")
        header=article.find_element_by_class_name("entry-title")
        print(header.text)

except:
    driver.quit()


#
# time.sleep(30)
driver.close()
#for commiting