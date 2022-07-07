""" 搜索结果页面"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from code.xueqiu_po_demo.base.xueqiu_app import XueQiuApp


class SearchResultPage(XueQiuApp):



    def goto_stock_tab(self, title):
        # click 股票 标题

        # self.driver.find_element_by_xpath().click()
        locator =(MobileBy.XPATH,f"//*[contains(@resource-id,'title_container')]//*[@text='{title}']")
        self.find_and_click(*locator)
        return self

    def get_price(self, stock_id):
        # 找到 阿里巴巴(stock_price) 对应的股票价格
        locator = (
            MobileBy.XPATH, f"//*[@text='{stock_id}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")

        # 显示等待
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        current_price = self.find_and_gettext(*locator)

        return float(current_price)
