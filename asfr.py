from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

#
opts = Options()
# opts.add_argument("--headless")
base_url = 'https://app.studi.fr/v3/login'
planning_url = 'https://app.studi.fr/#/dashboard/planning'
parcours_list_selector = 'div[ng-repeat="parcours in vm.mediatheque.parcours"] h4'
planning_item_title_class = "planning-item-detail-title"

driver = Firefox(options=opts)
driver.get(base_url)
timeout = 10
email = "narfin.d@gmail.com"
pwd = "1Loup@Studi"

try:
    #
    button_present = ec.presence_of_element_located((By.CLASS_NAME, 'mat-button-wrapper'))
    WebDriverWait(driver, timeout).until(button_present)
    driver.find_element(By.ID, "mat-input-0").send_keys(email)
    driver.find_element(By.ID, "mat-input-1").send_keys(pwd)
    driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()
    #

except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print(driver.title)
    driver.get(planning_url)

try:
    #
    parcours_list_present = ec.presence_of_element_located((By.CSS_SELECTOR, parcours_list_selector))
    WebDriverWait(driver, timeout).until(parcours_list_present)
    driver.find_element(By.CSS_SELECTOR, parcours_list_selector).click()
    #
    planning_item_present = ec.presence_of_element_located((By.CLASS_NAME, planning_item_title_class))
    WebDriverWait(driver, timeout).until(planning_item_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    number_of_course = len(driver.find_elements(By.CLASS_NAME, planning_item_title_class))
    print("courses in list: ", number_of_course)
    print(driver.title)
    # driver.close()
