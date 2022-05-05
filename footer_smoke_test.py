from selenium import webdriver

Botanika_URL = "https://botanikabeauty.com/"
driver = webdriver.Chrome(executable_path="Driver/chromedriver")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()

about_us_btn = driver.find_element_by_xpath('//a[@href="/pages/about-us"]')
about_us_btn.click()

terms_of_service = driver.find_element_by_xpath('//a[@href="/pages/terms-of-service"]')
terms_of_service.click()

return_policy = driver.find_element_by_xpath('//a[@href="/pages/return-policy"]')
return_policy.click()

driver.close()
driver.quit()
