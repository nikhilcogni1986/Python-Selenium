from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
actual_text = alert.text
validate_text = "Option3"

assert validate_text in actual_text
alert.accept()
driver.close()