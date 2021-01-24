from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

driver.find_element_by_id("name").send_keys("TEST THE ALERT")
driver.find_element_by_id("checkBoxOption1").click()

driver.find_element_by_css_selector("input[value='radio1']").click()
print(driver.find_element_by_css_selector("input[value='radio1']").is_selected())

driver.find_element_by_css_selector("#hide-textbox").click()
print("Text Box is now displayed --> ", driver.find_element_by_css_selector("#displayed-text").is_displayed())

driver.find_element_by_css_selector("#show-textbox").click()
print("Text Box is now displayed --> ", driver.find_element_by_css_selector("#displayed-text").is_displayed())

driver.close()