from selenium import    webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH,"//input[@type='submit' and @class='wikipedia-search-button']").click()

driver.find_element(By.XPATH,"//a[text()='Selenium']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[text()='Selenium in biology']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[text()='Selenium (software)']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[text()='Selenium disulfide']").click()

windows=driver.window_handles
for i in range(len(windows)):
    driver.switch_to.window(windows[0])
    i.click()


time.sleep(5)