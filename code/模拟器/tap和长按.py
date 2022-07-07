#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestSearch:
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装、权限设置操作
        desired_caps['autoAcceptAlerts'] = 'true'  # 默认选择接受弹窗的条款，有些app启动的时候，会有一些权限的弹窗
        desired_caps['noReset'] = "true"
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_touchAction(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("雪球")').click()

        myAction = TouchAction(self.driver)  # 实例化一个TouchAction对象

        window_rect = self.driver.get_window_rect()  # 获取整个屏幕的右下角的坐标window_rect={'width': 936, 'height': 1664, 'x': 0, 'y': 0}

        width = window_rect["width"]  # 提取屏幕的最大的宽

        height = window_rect['height']  # 提取屏幕的最大的高度

        x_start_end = int(width / 2)  # x的坐标定义为最大宽的一半，也就是中心的x坐标 [上下滑动 x 不变]

        y_start = int(height * 4 / 5)  # 定义起始的y坐标，在4/5的底部位置

        y_end = int(height * 1 / 5)  # 定义终点的y坐标，在1/5顶部的位置，这样就可以模拟从下往上滑动的动作

        # 先press点击初始的坐标，然后按住不放等2秒再move_to到终点坐标，然后再release()释放坐标点，
        myAction.press(x=x_start_end, y=y_start)\
                .wait(3000)\
                .move_to(x=x_start_end, y=y_end)\
                .release()\
                .perform()  # 最后用perform()去执行一系列action操


        # 总结：手机端端坐标轴中心点是从 左上角开始 从左往右的横线是x 从上往下点竖轴是y
