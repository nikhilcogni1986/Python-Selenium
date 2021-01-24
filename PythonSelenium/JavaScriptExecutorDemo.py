from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# click on shop button
shop_menu = driver.find_element_by_link_text("Shop")
driver.execute_script('arguments[0].click()', shop_menu)
driver.execute_script("window.scrollTo(0,500);")
driver.close()