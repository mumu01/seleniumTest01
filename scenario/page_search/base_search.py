# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By


class BaseSearch:

    def click_tab_video(self, driver):
        xpath = "//p[text()='Videos']"
        driver.find_element(By.XPATH, xpath).click()


    def get_video_count(self, driver):
        # get video list
        xpath = "//div[@id='__next']/div[1]/div[1]/div[1]/main[1]/div[1]"
        table_rows = driver.find_element(By.XPATH, xpath)
        count = table_rows.find_elements(By.TAG_NAME, 'h4')
        print('count = %s ' % len(count))
        count_value = len(count) + 1

        return count_value


    def check_user_name(self, driver, count_value, user_name):

        for i in range(1, count_value):
            time.sleep(0.5)
            # get name xpath
            xpath = "(//div[@class='Layout-sc-nxg1ff-0 jLsLts']//p)[%s]" % i
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, xpath))
            video_user_name = str(driver.find_element(By.XPATH, xpath).text)

            print('No%s = %s ' % (i, video_user_name))
            if video_user_name == user_name:
                # 找到同名 點擊進入
                v_xpath = "(//div[@class='Layout-sc-nxg1ff-0 fa-DJcD'])[%s]" % i
                driver.find_element(By.XPATH, v_xpath).click()

                time.sleep(5)
                videoPlayer = driver.find_element(By.CSS_SELECTOR, "video")
                driver.execute_script("return arguments[0].play();", videoPlayer)
                time.sleep(20)
                return True

            # list.append(video_user_name)


    def into_detail(self, driver):
        v_xpath = "(//div[@class='Layout-sc-nxg1ff-0 fa-DJcD'])[%s]" % 10
        driver.find_element(By.XPATH, v_xpath).click()

        time.sleep(10)
        videoPlayer = driver.find_element(By.CSS_SELECTOR, "video")
        play_result = driver.execute_script("return arguments[0].play();", videoPlayer)

        time.sleep(20)

        print(play_result)