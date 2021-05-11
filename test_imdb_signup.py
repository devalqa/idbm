"""
imdb.com Assignment from vahak
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
# chrome_option.add_argument("headless")
chrome_option.add_argument(("--ignore-certificate-errors"))
chrome_option.add_argument("--disable-gpu")


class Test_imdb():  # TC-01
    @pytest.fixture(scope="class")
    def test_imdb_title(self):
        global driver
        driver = webdriver.Chrome \
            (executable_path="..//Drivers/chromedriver 4", options=chrome_option)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://www.imdb.com/")
        print(driver.title)
        print(driver.current_url)
        yield
        driver.quit()

    def test_signup(self, test_imdb_title):  # Tc_02
        sign_in = driver.find_element_by_xpath("//div[contains(text(),'Sign In')]")
        sign_in.is_displayed()
        sign_in.click()
        create_ac_btn = driver.find_element_by_link_text("Create a New Account")
        create_ac_btn.is_enabled()
        create_ac_btn.click()
        btn_imdb_ac = driver.find_element_by_css_selector('#continue')
        if btn_imdb_ac.is_enabled():
            print("even no data filled btn is enabled Priorty:High serv: Low")
        else:
            ("test pass")
        btn_imdb_ac.click()
        time.sleep(2)
        driver.get_screenshot_as_file(
            "..//Screenshots/error.png")  # error would throw if click on create imdb ac without enter data

    def test_signup2(self, test_imdb_title):  # Tc_03
        driver.find_element_by_id("ap_customer_name").send_keys("deval")
        driver.find_element_by_id("ap_email").send_keys("devalth8gmail.com")
        driver.find_element_by_id("ap_password").send_keys("1234567890")
        driver.find_element_by_id("ap_password_check").send_keys("1234567890")
        driver.find_element_by_css_selector('#continue').click()
        time.sleep(2)
        driver.find_element_by_id("ap_customer_name").clear()
        driver.find_element_by_id("ap_customer_name").send_keys("deval")
        driver.find_element_by_id("ap_password").clear()
        driver.find_element_by_id("ap_password").send_keys("@@1##11(")
        driver.find_element_by_id("ap_password_check").clear()
        driver.find_element_by_id("ap_password_check").send_keys("@@1##11(")
        driver.find_element_by_css_selector('#continue').click()
        time.sleep(2)
        driver.get_screenshot_as_file("..//Screenshots/credentialerror.png")
    def test_signup_valid(self,test_imdb_title):    #Tc_04
        driver.find_element_by_id("ap_customer_name").send_keys("deval")#use your own name
        driver.find_element_by_id("ap_email").send_keys("devalth8@gmail.com")# use your own email id not this(demo)
        driver.find_element_by_id("ap_password").send_keys("12345678")# use your own pass (demo)
        driver.find_element_by_id("ap_password_check").send_keys("12345678")
        driver.find_element_by_css_selector('#continue').click()




