from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

OuterFrame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(OuterFrame)

innerFrame=driver.find_element(By.XPATH,"//h5[text()='Nested iFrames']/following::iframe")
driver.switch_to.frame(innerFrame)

# driver.find_element(By.XPATH,"//input[@type='text']").send_keys("hello")

