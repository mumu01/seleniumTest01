# -*- coding: utf-8 -*-
import time
from scenario.page_search import base_search

class ControlSearch:


    def check_video_name(self, driver, video_count_value, user_name):
        for i in range(3):

            search_action = base_search.BaseSearch
            result = search_action.check_user_name(self, driver, video_count_value, user_name)

            if result:
                # true = 找到同名離開, false = 繼續找
                break

            if i == 2:
                # 沒找到就撥最後一筆
                search_action.into_detail(self, driver)

            time.sleep(1)
            driver.execute_script("window.scrollTo(0,-2000)")