from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def check_presence_of(driver_to_use, time_out: float, element_to_locate, exit_on_fail=True):
    """Check presence of an element.
    'driver' is the Webdriver used to navigate in the page.
    'time_out' define the delay while we wait element presence.
    'element_to_locate' selenium expected element to locate
    'exit_on_fail' define if we stop the script when element is not found.
    """
    try:
        WebDriverWait(driver_to_use, time_out).until(element_to_locate)
    except TimeoutException:
        print("Timed out waiting for page to load")
        if exit_on_fail:
            exit(1)
