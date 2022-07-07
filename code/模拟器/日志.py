#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import pytest
from appium import webdriver


class TestLog():
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_log(self):
        logging.info("点击输入框控件")
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_banner").click()

        logging.info("输入搜索的内容：阿里巴巴")
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()

        current_price = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text

        logging.info(f"当前09988 对应的股价价格是：{current_price}")

        assert float(current_price) < 200

"""
总结
1：需要再项目的根目录添加 pytest.ini  【可参考如下连接】
2: 自定义日志文件名字 可创建conftest.py文件

【https://ceshiren.com/t/topic/13105】


"""







if __name__ == '__main__':
    pytest.main()
