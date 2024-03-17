from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"(//p[@class='oxd-text oxd-text--p orangehrm-copyright'])[2]/a").click()

windows=driver.window_handles
# parent=windows[0]
# print(parent)
# driver.switch_to.window(parent)
# print(driver.title)

# child=windows[1]
# print(child)
# driver.switch_to.window(child)
# print(driver.title)

for window in windows:
    driver.switch_to.window(window)
    if driver.title=="Human Resources Management Software | OrangeHRM":
        driver.close()

time.sleep(10)









    








