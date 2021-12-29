# -*- coding: utf-8 -*-


from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BaseDetail:


    def click_search_btn(self, driver):
        xpath = "//body/div[@id='__next']/div[1]/div[1]/div[1]/nav[1]/div[2]/div[2]/a[1]/button[1]"
        driver.find_element(By.XPATH, xpath).click()


    def input_search_content(self, driver, input_value):
        xpath = "//input[@type='search']"
        driver.find_element(By.XPATH, xpath).send_keys(input_value)


    def enter_search(self, driver):
        xpath = "//input[@type='search']"
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)