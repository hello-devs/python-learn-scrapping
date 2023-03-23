from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

#
opts = Options()
opts.add_argument("--headless")
browser = Firefox(options=opts)
# browser = Firefox()
browser.get('https://httpbin.org/headers')

print(browser.find_element(By.ID, 'json').text)
