from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("all-packages-table")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()

# driver.find_element(By.LINK_TEXT,"WebDriver").click()
# driver.find_element(By.LINK_TEXT,"Help").click()





time.sleep(5)

