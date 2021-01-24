import time

from selenium import webdriver

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
    add_cart_button.click()

# click on Cart button
driver.find_element_by_css_selector("img[alt='Cart']").click()

# Click to proceed to checkout
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# Enter promo code
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").is_displayed())
driver.close()