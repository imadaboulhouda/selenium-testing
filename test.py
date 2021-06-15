from selenium import webdriver
option = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=option)
el = driver.get("https://imadaboulhouda.com")
data = driver.find_elements_by_css_selector("img")
for d in data:
	print(d.get_attribute('src'))
#print(data)

