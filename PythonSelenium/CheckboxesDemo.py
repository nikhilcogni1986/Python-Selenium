from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print("Number of checkboxes are: ", len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()
driver.close()
