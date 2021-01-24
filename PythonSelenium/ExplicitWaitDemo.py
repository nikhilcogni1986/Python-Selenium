import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list1 = []
list2 = []

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("Ber")
time.sleep(1)

vegetables = driver.find_elements_by_xpath("//div[@class='products']/div")
number_of_vegetables = len(vegetables)
assert number_of_vegetables == 3

# Clicking on Add Cart buttons
add_cart_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for add_cart_button in add_cart_buttons:
    list1.append(add_cart_button.find_element_by_xpath("parent::div/parent::div/h4").text)
    add_cart_button.click()
print(list1)

# click on Cart button
driver.find_element_by_css_selector("img[alt='Cart']").click()

# Click to proceed to checkout
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# get the original amount before discount
orginal_amount = driver.find_element_by_css_selector("span.discountAmt").text

# Enter promo code
wait = WebDriverWait(driver, 15)
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()

# get the vegetables List
veggiesList = driver.find_elements_by_css_selector("p.product-name")

for veg in veggiesList:
    list2.append(veg.text)
print(list2)

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

# get the discounted amount
discounted_amount = driver.find_element_by_css_selector("span.discountAmt").text
print("Cart value before discount", orginal_amount)
print("Cart value after discount", discounted_amount)


# check whether discounted amount is less than original amount
assert float(discounted_amount) < int(orginal_amount)

# compare 2 lists
assert list1 == list2

# grab the product prices for each vegetable and verify the sum
prices = driver.find_elements_by_xpath("//tr/td[5]/p")
FinalAmount = 0

for product_price in prices:
    FinalAmount = FinalAmount + int(product_price.text)

total_amount = int(driver.find_element_by_xpath("//span[@class='totAmt']").text)
assert FinalAmount == total_amount
driver.close()