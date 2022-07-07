from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from code.xueqiu_po_demo.base.xueqiu_app import XueQiuApp
from code.xueqiu_po_demo.page.search_page import SearchPage

""" app的主页面"""


class MainPage(XueQiuApp):


    # 定位搜索框--》点击-->进入搜索界面
    def click_search(self):
        locator = (MobileBy.ID, "com.xueqiu.android:id/tv_banner")
        self.find(*locator).click()
        return SearchPage(self.driver)
