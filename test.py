from selenium import webdriver
driver_location =  "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"
option = webdriver.ChromeOptions()
option.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,chrome_options=option)
el = driver.get("https://imadaboulhouda.com")
data = driver.find_elements_by_css_selector("img")
for d in data:
	print(d.get_attribute('src'))
#print(data)

