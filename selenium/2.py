from selenium import    webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()



driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile")
driver.find_element(By.ID,"nav-search-submit-button").click()

driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[2]").click()
element = driver.find_element(By.XPATH,"(//span[@class='a-color-base a-text-bold'])[1]").text
print(element)






