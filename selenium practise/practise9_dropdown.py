from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

alloptions=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))

alloptions.select_by_index(5)
time.sleep(5)

alloptions.select_by_value("india")
time.sleep(5)

alloptions.select_by_visible_text("Japan")
time.sleep(10)



driver.quit()
