import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

driver.find_element_by_id("autocomplete").send_keys("Ind")
time.sleep(2)

countries = driver.find_elements_by_xpath("//li[@class='ui-menu-item']")
print(len(countries))
print(type(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autocomplete").text)
assert driver.find_element_by_id("autocomplete").get_attribute("value") == "India"

driver.get("https://www.yatra.com/")
driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']").click()
time.sleep(2)

driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']").send_keys("Del")
from_city_options = driver.find_elements_by_xpath("//div[@class='ac_airport']//p[@class='ac_airportname']")
print(len(from_city_options))
print(type(from_city_options))

for city in from_city_options:
    if city.text == "Delhi":
        city.click()
        break

assert driver.find_element_by_xpath("//label[@for='BE_flight_origin_city']//div/p").text == "DEL"

driver.close()
