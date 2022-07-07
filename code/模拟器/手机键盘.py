#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch:
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['skipServerInstallation'] = True
        desired_caps['UiAutomator'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_keyEvent(self):

        print("back")
        self.driver.keyevent(4)
        time.sleep(3)

        print("home")
        self.driver.keyevent(3)
        time.sleep(2)

        print("lock")
        self.driver.lock(4)
        time.sleep(3)

    def test_log(self):
        types = self.driver.get_performance_data_types()
        print(types)
        time.sleep(10)
        print(self.driver.get_performance_data("com.xueqiu.android", 'cpuinfo', 10))
