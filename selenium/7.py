from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.google.com/")

driver.maximize_window()

mywait=WebDriverWait(driver,10,ignored_exceptions=Exception)
search=mywait.until(EC.presence_of_element_located((By.XPATH,"*//[@title='Search'")))
search.submit()



