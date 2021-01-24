from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
chrome_options.add_argument("window-size=1500,1200")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(executable_path="F:\\Selenium\\src\\main\\Resources\\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.close()