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

    def test_call_phone(self):
        # only for android
        self.driver.make_gsm_call("13801010101", GsmCallActions.CALL)

    def test_sms(self):
        self.driver.send_sms('13801010101', 'Hey lol...')
        # 执行完之后，去信息里面看是否有收到短信

    #  黏贴版
    def test_copy_save(self):
        self.driver.set_clipboard_text()
        self.driver.get_clipboard_text()

    def test_network(self):
        print(self.driver.network_connection)
        self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)  # 飞行模式
        print(self.driver.network_connection)

        time.sleep(3)  # 为了调试时可以看到网络切换都过程
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)  # 所有网络都打开

    # 录屏
    def test_luPing(self):
        # ps: 受限手机和版本 比如华为  比如只能android8.0以上

        # self.driver.start_recording_screen()
        # do_something
        # self.driver.stop_recording_screen()
        pass

    # 截图
    def test_screenShot(self):
        # 把当前页面截图到指定目录下[提前创建好images目录]
        # 只支持安卓8.0以上
        self.driver.get_screenshot_as_file('./images/login.png')

