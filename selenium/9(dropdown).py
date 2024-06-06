from selenium import    webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

dropdown=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))

all=dropdown.options
for i in all:
    print(i.text)


# print(len(all))
# dropdown.select_by_visible_text("India")
# dropdown.select_by_value("usa")
# dropdown.select_by_index(0)

# for i in all:
#     if i.text=='India':
#         i.click()
# last_option=all[-1]
# last_option.click()


time.sleep(5)

