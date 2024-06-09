from selenium import webdriver
from selenium.webdriver.common.by import By
import xlutils

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)
driver.maximize_window


file='C:\\Users\\tika-btm-ltp158\\Desktop\\Selenium-in-DDT.xlsx'
rows=xlutils.getrowcount(file,'Sheet1')

for r in range(2,rows+1):
    username=xlutils.readdata(file,'Sheet1',r,1)
    password=xlutils.readdata(file,'Sheet1',r,2)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    if driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
        print("login passed")
        xlutils.writedata(file,'Sheet1',r,4,data="passed")
        xlutils.greencolor(file,'Sheet1',r,4)
        driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
        driver.find_element(By.XPATH,"//a[text()='Logout']").click()

    else:
        print("login failed")
        xlutils.writedata(file,'Sheet1',r,4,data="failed")
        xlutils.redcolor(file,'Sheet1',r,4)


