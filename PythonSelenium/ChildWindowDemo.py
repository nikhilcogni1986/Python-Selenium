from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
child_window = driver.window_handles[1]

driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3").text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.close()