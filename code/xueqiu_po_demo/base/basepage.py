
"""基本的方法： find 、 click、 swipe"""
import logging

import time

from appium.webdriver.webdriver import WebDriver

from code.xueqiu_po_demo.base.black_handle import black_wrapper


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text

    # 截图
    def screenshot(self, path):
        logging.info(f"path shot =={path}")
        self.driver.get_screenshot_as_file(path)

    # 当前时间格式
    def get_current_time(self):
        return time.strftime("%Y-%m-%d-%H-%M-%S")

    # 截图名称
    def get_png_name(self, name):
        return self.get_current_time() + "-" +name + ".png"
