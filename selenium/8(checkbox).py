from selenium import webdriver
from    selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id,'day')]")

# for checkbox in checkboxes:
#     checkbox.click()
# time.sleep(5)

# for i in range(len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(5)

# for checkbox in checkboxes:
#     name=checkbox.get_attribute('id')
#     if name=='monday' or name=='saturday':
#         checkbox.click()
# time.sleep(5)
        
# for i in range(len(checkboxes)):
#     if i>3:
#         checkboxes[i].click()

# time.sleep(5)

# for i in range(len(checkboxes)):
#     if i>3:
#         checkboxes[i].is_selected()
#         checkboxes[i].click()

# time.sleep(5)



driver.quit()

