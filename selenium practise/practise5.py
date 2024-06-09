from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By.XPATH,"//input[@name='Email']")
emailbox.clear()
emailbox.send_keys("abc@xyz.com")
print(emailbox.get_attribute("value"))






