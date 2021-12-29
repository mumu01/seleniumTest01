# -*- coding: utf-8 -*-

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scenario.page_home import base_home
from scenario.page_search import base_search
from scenario import control_search

class TestMain():
  def setup_method(self, method):

    chrome_options = Options()
    mobileEmulation = {'deviceName': 'iPhone X'}
    chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)

    self.driver = webdriver.Chrome(chrome_options=chrome_options)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_script(self):

    self.driver.get("https://m.twitch.tv/")
    # self.driver.maximize_window()

    home_action = base_home.BaseHome

    # -- index
    home_action.click_search_btn(self, self.driver)
    home_action.input_search_content(self, self.driver, "Monster Hunter World")
    home_action.enter_search(self, self.driver)

    time.sleep(1)

    # -- video list
    search_action = base_search.BaseSearch

    search_action.click_tab_video(self, self.driver)

    # retrun 影片列表有幾筆
    count_value = search_action.get_video_count(self, self.driver)

    #
    control_search.ControlSearch.check_video_name(self, self.driver, count_value, 'CervelloneRe' )

if __name__ == '__main__':
        pytest.main(['-s', 'main.py'])