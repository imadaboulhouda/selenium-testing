from selenium import webdriver
option = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.youtube.com/")
driver.find_elements_by_css_selector('#search')[0].send_keys('Vadim')
driver.find_elements_by_css_selector('#search-icon-legacy')[0].click()
data = driver.find_elements_by_css_selector('#video-title.ytd-video-renderer')
print(data)
for d in data:
	print(d.text)

