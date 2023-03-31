import wget
from itertools import chain
from selenium.webdriver import Firefox
# from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec

from tools import scrap_tools as sc

#
opts = Options()
opts.add_argument("--headless")
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


def get_courses():
    courses_presence = ec.presence_of_element_located((By.CLASS_NAME, "ressource-title"))
    sc.check_presence_of(driver, timeout, courses_presence)

    return driver.find_elements(By.CLASS_NAME, "ressource-title")


#
planning_items = get_first_parcours_items()

number_of_course = len(planning_items)
print("courses in list: ", number_of_course)

# dismiss cookie
dismissBtn = ec.presence_of_element_located((By.CSS_SELECTOR, "a.cc-dismiss"))
sc.check_presence_of(driver, timeout, dismissBtn)
btn_cookie = driver.find_element(By.CSS_SELECTOR, "a.cc-dismiss")
btn_cookie.click()

file = open(file="liste-cours.txt", mode="a", encoding="utf-8")

# for i in chain(range(0, 22), range(23, 47)):
for i in range(34, 47):
    # for i in range(number_of_course):
    # last module is empty
    if i == 47:
        break

    item = planning_items[i]
    print(str(i) + " __ " + item.text)
    file.write(str(i) + " __ " + item.text + "\n")
    driver.execute_script(f'arguments[0].click();', item)

    courses = get_courses()

    for j in range(len(courses)):
        if i == 29 and j == 2:
            # le cours est composé de video
            continue
        if i == 34 and not j == 0:
            # passage obligatoire minimum cookie
            continue
        if i in range(35, 46):
            continue
        if i == 46 and j in range(0, 9):
            continue

        print(str(j) + ": " + courses[j].text)
        file.write(courses[j].text + "\n")
        courses[j].click()
        #
        course_iframe = ec.presence_of_element_located((By.ID, 'courseframecontent'))
        sc.check_presence_of(driver, timeout, course_iframe)
        course_link = driver.find_element(By.ID, 'courseframecontent').get_attribute('src')
        # print(course_link)
        driver.get(course_link)
        #
        course_content_iframe = ec.presence_of_element_located((By.ID, 'course-iframe'))
        sc.check_presence_of(driver, timeout, course_content_iframe)
        course_content_link = driver.find_element(By.ID, 'course-iframe').get_attribute('src')
        # print(course_content_link)
        driver.get(course_content_link)
        #
        start_btn_presence = ec.presence_of_element_located((By.CSS_SELECTOR, "a.btnNav.start"))
        sc.check_presence_of(driver, timeout, start_btn_presence)
        driver.find_element(By.CSS_SELECTOR, "a.btnNav.start").click()
        #
        pdf_btn_presence = ec.presence_of_element_located((By.CSS_SELECTOR, 'li.print a'))
        sc.check_presence_of(driver, timeout, pdf_btn_presence)
        pdf_btn = driver.find_element(By.CSS_SELECTOR, 'li.print a')
        pdf_url = pdf_btn.get_attribute("href")

        # wget.download(pdf_url, "courses/")

        print(pdf_url)
        file.write(pdf_url + "\n")

        driver.back()
        driver.back()
        driver.back()
        driver.back()
        courses = get_courses()

    driver.back()
    planning_items = get_first_parcours_items()

driver.close()
file.close()
