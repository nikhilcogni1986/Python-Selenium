from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

# switch to frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Iam ready to automate")
driver.close()