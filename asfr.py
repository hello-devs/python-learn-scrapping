from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from tools import scrap_tools as sc

#
opts = Options()
# opts.add_argument("--headless")
base_url = 'https://app.studi.fr/v3/login'
planning_url = 'https://app.studi.fr/#/dashboard/planning'
parcours_list_selector = 'div[ng-repeat="parcours in vm.mediatheque.parcours"] h4'
planning_item_title_class = "planning-item-detail-title"

driver = Firefox(options=opts)
driver.get(base_url)
timeout = 5.
email = "narfin.d@gmail.com"
pwd = "1Loup@Studi"

# Check Login page load
button_present = ec.presence_of_element_located((By.CLASS_NAME, 'mat-button-wrapper'))
sc.check_presence_of(driver, timeout, button_present)
# Fill Form and connect
driver.find_element(By.ID, "mat-input-0").send_keys(email)
driver.find_element(By.ID, "mat-input-1").send_keys(pwd)
driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()

# Check menu load
menu_present = ec.presence_of_element_located((By.CSS_SELECTOR, "ul.list-menu"))
sc.check_presence_of(driver, timeout, menu_present)
# Go to planning Page
driver.get(planning_url)

# Check parcours list load
parcours_list_present = ec.presence_of_element_located((By.CSS_SELECTOR, parcours_list_selector))
sc.check_presence_of(driver, timeout, parcours_list_present)
# Select first parcours
driver.find_element(By.CSS_SELECTOR, parcours_list_selector).click()

# Check course list load
planning_item_present = ec.presence_of_element_located((By.CLASS_NAME, planning_item_title_class))
sc.check_presence_of(driver, timeout, planning_item_present)

# count number of course
planning_items = driver.find_elements(By.CLASS_NAME, planning_item_title_class)
number_of_course = len(planning_items)
print("courses in list: ", number_of_course)

planning_items[0].click()
# driver.close()
