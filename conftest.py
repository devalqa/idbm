"""
conftest fixture
"""
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import sys
from pytest import fixture
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
#chrome_option.add_argument("headless")
chrome_option.add_argument(("--ignore-certificate-errors"))
chrome_option.add_argument("--disable-gpu")


@pytest.fixture(scope="class")
def test_setup_vahan(request):
    _driver =None
    _driver = webdriver.Chrome \
        (executable_path="..//Drivers/chromedriver 4",options=chrome_option)
    _driver.maximize_window()
    _driver.implicitly_wait(20)
    _driver.get("https://www.imdb.com/")
    time.sleep(2)
    print(_driver.title)
    print(_driver.current_url)
    sign_in =_driver.find_element_by_xpath("//div[contains(text(),'Sign In')]")
    _driver.execute_script("arguments[0].click();",sign_in)
    imdb=_driver.find_element_by_xpath("//span[normalize-space()='Sign in with IMDb']")
    _driver.execute_script("arguments[0].click();",imdb)
    _driver.find_element_by_id("ap_email").send_keys("devalth8@gmail.com")  # use your own email id not this(demo)
    _driver.find_element_by_id("ap_password").send_keys("12345678")  # use your own pass (demo)
    _driver.find_element_by_css_selector("#signInSubmit").click()
    request.cls.driver =_driver
    yield request.cls.driver
    request.cls.driver.quit()

