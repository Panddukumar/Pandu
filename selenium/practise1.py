from selenium import webdriver
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# get_text=driver.find_element(By.XPATH,"//a[contains(text(),'Tata Consumer Produc')]").text

# get_text=driver.find_element(By.XPATH,"//a[contains(text(),'HUDC')]/following::tr[1]/td[1]").text

# get_text=driver.find_elements(By.XPATH,"//a[contains(text(),'HUDC')]/ancestor::tr/child::td").text

# get_text=driver.find_element(By.XPATH,"//a[contains(text(),'HUDC')]/ancestor::tr/following-sibling::tr[1]").text

get_text=driver.find_element(By.XPATH,"//a[contains(text(),'HUDC')]/ancestor::tr/preceding-sibling::tr[1]").text


print(len(get_text))
print(get_text)

exp_text='Tata Consumer Produc'
if get_text==exp_text:
    print("success")
else:
    print("failure")



