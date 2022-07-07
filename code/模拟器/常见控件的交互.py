#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


class TestDW():
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.android.settings'  # 设置应用
        desired_caps['appActivity'] = 'com.android.settings.Settings'  # 首页面

        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装、权限设置操作
        # 当我们使用appium运行测试用例的时候，会在我们手机中安装一个appium setting的apk，
        # 每次安装这个应用都会消耗一定的时间。
        # skipDeviceInitialization参数就是在我们运行的时候去检查手机是否安装了此应用，
        # 当安装完以后则会跳过这个步骤。起到一个提高效率，节省时间的作用

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_ele(self):

        self.driver.find_element_by_accessibility_id("Animation").click()
        self.driver.find_element_by_accessibility_id("Seeking").click()
        runButton = self.driver.find_element_by_accessibility_id("Run")

        runButton.is_displayed()
        isClickable = runButton.get_attribute("clickable")
        assert isClickable == True


if __name__ == '__main__':
    pytest.main()
