import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

actions = ActionChains(driver)
webelement_mouseover = driver.find_element_by_id("mousehover")

actions.move_to_element(webelement_mouseover).perform()
webelement_reload = driver.find_element_by_link_text("Reload")
time.sleep(2)
actions.move_to_element(webelement_reload).click().perform()
driver.close()