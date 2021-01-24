from selenium import webdriver

driver = webdriver.Firefox(executable_path="D:\\Selenium Essentials\\Jars\\geckodriver-v0.28.0-win64\\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
print(driver.title)
print(driver.current_url)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.back()
driver.minimize_window()
driver.close()