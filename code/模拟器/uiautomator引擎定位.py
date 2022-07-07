#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import pytest
from appium import webdriver


class TestDW():
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()


    """
    特点：因为是andriod自带的引擎，所以速度快
         但是语法复杂 ide也不提示
    """
    def test_myInfo(self):
        """
        1,  点击我的 ， 进入到个人信息页面
        2， 点击登录，进入到登录页面
        3， 输入用户名，输入密码，
        4， 点击登录

        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_zuhe(self):
        """
        1,  点击我的 ， 进入到个人信息页面
        2， 点击登录，进入到登录页面
        3， 输入用户名，输入密码，
        4， 点击登录

        :return:
        """

        # 组合定位
        resourceId_text = 'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")'
        self.driver.find_element_by_android_uiautomator(resourceId_text).click()

        resourceId_text_childSelector = 'new UiSelector().resourceId("com.xueqiu.android: id / title_container").childSelector(text("股票"))'
        self.driver.find_element_by_android_uiautomator(resourceId_text_childSelector)

    def test_scroll_find_element(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("热榜")').click()

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().resourceId("com.xueqiu.android:id/tv_status_index").text("17").'
                                                        'instance(0));').click()
        time.sleep(5)


if __name__ == '__main__':
    pytest.main()
