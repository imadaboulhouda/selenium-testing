from selenium import webdriver
option = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.imdb.com/find?q=test&ref_=nv_sr_sm")

#driver.find_elements_by_css_selector('#search-icon-legacy')[0].click()
data = driver.find_elements_by_css_selector('.findSection')
print(data)
for d in data:
	print(d.find_element_by_css_selector('.result_text').text)

