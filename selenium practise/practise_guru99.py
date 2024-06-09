from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/")
elements=driver.find_elements(By.TAG_NAME,"tr")
print(len(elements))


# driver.find_element(By.NAME, "userName").send_keys("tutorial")
# driver.find_element(By.NAME, "password").send_keys("tutorail")
# driver.find_element(By.NAME, "submit").click()




driver.quit()
