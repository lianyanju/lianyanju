#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait:
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        pass

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_banner").click()
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        isEnable = search_ele.is_enabled()
        if isEnable:
            search_ele.send_keys("alibaba")
            self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
            self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()

            locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")

            # 普通表达法
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
            ele = self.driver.find_element(*locator)

            # lambda表达法
            # ele = WebDriverWait(self.driver,10).until( lambda x: x.find_element(*locator))


            current_price = float(ele.text)
            expect_price = 170
            assert current_price > expect_price

        else:
            print("00000000000")
