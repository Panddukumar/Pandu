from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://docs.python.org/3/tutorial/")

# Wait for the list of links to load
wait = WebDriverWait(driver, 10)
all_links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//li[@class='toctree-l1']//a")))

print(len(all_links))

for link in all_links:
    url = link.get_attribute("href")
    driver.execute_script("window.open('"+url+"','_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    print(driver.current_url)
