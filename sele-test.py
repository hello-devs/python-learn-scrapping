from selenium.webdriver import ChromiumEdge
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

#
# opts = Options()
# opts.add_argument("--headless")
# browser = Firefox(options=opts)
browser = ChromiumEdge()
browser.implicitly_wait(3600)
# browser = Firefox()
browser.get('https://httpbin.org/headers')

# print(browser.find_element(By.ID, 'json').text)
