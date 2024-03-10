from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/")
driver.find_element(By.NAME, "userName").send_keys("tutorial")
driver.find_element(By.NAME, "password").send_keys("tutorail")
driver.find_element(By.NAME, "submit").click()

element = driver.find_element

# Get the text of the element
element_text = element.text

act_title=driver
exp_title="Mercury Tours"
if act_title==exp_title:
    print("login test passed")
else:
    print("login test failed")

driver.quit()
