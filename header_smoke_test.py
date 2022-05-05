from selenium import webdriver

Botanika_URL = "https://botanikabeauty.com/"
driver = webdriver.Chrome(executable_path="Driver/chromedriver")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()

facebook_btn = driver.find_element_by_xpath('//i[@class="icon-facebook"]')
facebook_btn.click()

twitter_btn = driver.find_element_by_xpath('//i[@class="icon-twitter"]')
twitter_btn.click()

instagram_btn = driver.find_element_by_xpath('//i[@class="icon-instagram"]')
instagram_btn.click()

driver.close()
driver.quit()