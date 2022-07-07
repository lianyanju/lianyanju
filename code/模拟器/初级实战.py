#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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
        self.driver.implicitly_wait(40)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        """
               打开【雪球】应用首页
               定位首页的搜索框
               判断搜索框的是否可用,并查看搜索框name属性值
               打印搜索框这个元素的左上角坐标和它的宽高
               向搜索框输入 ：alibaba
               判断【阿里巴巴】是否可见
               如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
               :return:
         """
        search_key = 'alibaba'
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_banner").click()
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        isEnable = search_ele.is_enabled()
        if  isEnable == True:

            location = search_ele.location
            print("location==== ",location)

            size = search_ele.size
            print("size===",size)

            text = search_ele.text
            print("text=====",text)

            search_ele.click()
            search_ele.send_keys(search_key)
            res = self.driver.find_element_by_xpath("//*[@text='阿里巴巴']")
            if res.is_displayed():
                print("搜索成功")
                assert True
            else:
                print("搜索成功")
                assert False
        else:
            print("搜索成功")
            assert False
