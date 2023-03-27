from selenium.webdriver import Firefox
# from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec

from tools import scrap_tools as sc

#
opts = Options()
# opts.add_argument("--headless")
base_url = 'https://app.studi.fr/v3/login'
planning_url = 'https://app.studi.fr/#/dashboard/planning'
parcours_list_selector = 'div.planning-list-title'
planning_item_title_class = "planning-item-detail-title"

driver = Firefox(options=opts)
# driver = Chrome(options=opts)
# driver.maximize_window()
driver.get(base_url)
timeout = 10
email = "narfin.d@gmail.com"
pwd = "1Loup@Studi"

# Check Login page load
button_present = ec.presence_of_element_located((By.CLASS_NAME, 'mat-button-wrapper'))
sc.check_presence_of(driver, timeout, button_present)
# Fill Form and connect
driver.find_element(By.ID, "mat-input-0").send_keys(email)
driver.find_element(By.ID, "mat-input-1").send_keys(pwd)
driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()


def get_first_parcours_items():
    # Check menu load
    menu_present = ec.presence_of_element_located((By.CSS_SELECTOR, "ul.list-menu"))
    sc.check_presence_of(driver, timeout, menu_present)
    # print("menu present")
    # Go to planning Page
    driver.get(planning_url)

    # Check parcours list load
    parcours_list_present = ec.presence_of_element_located((By.CSS_SELECTOR, parcours_list_selector))
    sc.check_presence_of(driver, timeout, parcours_list_present)
    # print("parcours selector present")
    # Select first parcours
    driver.find_element(By.CSS_SELECTOR, parcours_list_selector).click()

    # Check course list load
    planning_item_present = ec.element_to_be_clickable((By.CLASS_NAME, planning_item_title_class))
    sc.check_presence_of(driver, timeout, planning_item_present)
    # print("planning item is clickable")
    # count number of course
    planning_items_to_return = driver.find_elements(By.CLASS_NAME, planning_item_title_class)

    return planning_items_to_return


planning_items = get_first_parcours_items()

number_of_course = len(planning_items)
print("courses in list: ", number_of_course)

# dismiss cookie
dismissBtn = ec.presence_of_element_located((By.CSS_SELECTOR, "a.cc-dismiss"))
sc.check_presence_of(driver, timeout, dismissBtn)
btn_cookie = driver.find_element(By.CSS_SELECTOR, "a.cc-dismiss")
btn_cookie.click()

for i in range(number_of_course):
    # last module is empty
    if i == 47:
        break

    item = planning_items[i]
    print(item.text)
    driver.execute_script(f'arguments[{i}].click();', item)

    # TODO loop throw course

    driver.back()
    planning_items = get_first_parcours_items()

# driver.close()
