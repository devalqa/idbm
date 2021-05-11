"""
vahan Assignment

"""
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import sys
from pytest import fixture






@pytest.mark.usefixtures('test_setup_vahan')
class Test_movies():
    def test_movies(self,test_setup_vahan):
        driver = test_setup_vahan
        Menu=driver.find_element_by_xpath\
            ("//label[@id='imdbHeader-navDrawerOpen--desktop']//*[local-name()='svg']")
        Menu.click()
        top_rate_movie =driver.find_element_by_xpath("//a[@role='menuitem'and @href='/chart/top/?ref_=nv_mv_250'and contains(normalize-space(),'Top Rated Movies')]")
        top_rate_movie.click()
        sort=driver.find_element_by_xpath("//select[@id='lister-sort-by-options']")
        drop_down=Select(sort)
        drop_down.select_by_visible_text("Release Date")
        desc_order=driver.find_element_by_css_selector("span[title='Descending order']")
        action = ActionChains(driver)
        action.click(desc_order).perform()
        time.sleep(2)
        driver.get_screenshot_as_file("..//Screenshots/sort.png")
        last_sort_movie=driver.find_element_by_link_text("The Kid")
        last_sort_movie.is_displayed()
        last_sort_movie.click()
        element= driver.find_element_by_css_selector("a[title='See more release dates']")
        final_output =element.text
        print(f" Hi Padmini & Prashant Release Date of a Movie 'The Kid' is {final_output} which is last sorted in Top Rated Movie Thanks.")
        time.sleep(2)
        driver.get_screenshot_as_file("..//Screenshots/sortedthekid.png")
        print(driver.current_url)








