#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_touchAction_tap(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_accessibility_id("Buttons").click()

        action = TouchAction(self.driver)

        # tap,对一个元素/控件/坐标 执行[点击]操作。用法参考press()
        # 解释：不是所有元素都像button有click属性 所以此时tap就发挥了作用
        action.tap(self.driver.find_element_by_accessibility_id("Toggle")).wait(3000).perform()

    def test_touchAction_swipe(self):
        self.driver.find_element_by_accessibility_id("Views").click()

        action = TouchAction(self.driver)

        action.long_press(x=550, y=200, duration=3000)\
              .move_to(x=550, y=550)\
              .release()\
              .perform()
