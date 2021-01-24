from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

assert "Page" in driver.title

dropdown = Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_index(1)
dropdown.select_by_value("option2")
dropdown.select_by_visible_text("Option3")

driver.close()