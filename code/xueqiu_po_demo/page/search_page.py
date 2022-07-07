
""" 搜索页面"""
from appium.webdriver.common.mobileby import MobileBy

from code.xueqiu_po_demo.base.xueqiu_app import XueQiuApp
from code.xueqiu_po_demo.page.search_result_page import SearchResultPage


class SearchPage(XueQiuApp):


    #定位输入框--》发送搜索内容
    def find_input_search(self, search_key):

        locator = (MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        self.find_and_send(*locator, search_key)

        return self

    # 定位搜索的结果--点击进入搜索结果页面
    def findout_searchresult(self,  text):
        locator = (MobileBy.XPATH, f"//*[@text='{text}']")
        self.find_and_click(*locator)
        return SearchResultPage(self.driver)