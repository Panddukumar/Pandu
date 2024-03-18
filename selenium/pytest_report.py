from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
   

def test_python_menu(driver):
    driver.get("https://www.python.org/")

    menu_items = driver.find_elements(By.CSS_SELECTOR, "#top ul.menu li")

    menu_titles = [item.text for item in menu_items]

    assert menu_titles, "No menu items found"

    # Output the extracted menu titles for verification
    print("Menu Titles:")
    for title in menu_titles:
        print(title)
