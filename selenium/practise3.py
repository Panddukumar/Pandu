from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))

elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(elements[0].text)

elements=driver.find_elements(By.XPATH,"//di[@class='footer']//a")
for ele in elements:
    print(ele.text)










