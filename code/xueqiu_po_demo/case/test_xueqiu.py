import logging

import pytest
from hamcrest import assert_that, close_to

from code.xueqiu_po_demo.base import operator_yml
from code.xueqiu_po_demo.base.xueqiu_app import XueQiuApp


class TestXueQiu:

    yaml_datas = operator_yml.get_data("../datas/searchdata.yml")
    logging.info(f"yaml文件数据是--------：{yaml_datas}")
    
    def setup_class(self):
        # 启动app
        self.xueqiuapp = XueQiuApp()

    def setup(self):
        self.mainpage = self.xueqiuapp.start().go_main()

    def teardown(self):
        pass

    def teardown_class(self):
        self.xueqiuapp.stop()

    """ 测试用例层，负责业务链式调用"""
    @pytest.mark.parametrize('search_key,text,tab_title,price', yaml_datas)
    def test_search(self, search_key, text, tab_title, price):

        stock_price = self.mainpage.click_search() \
            .find_input_search(search_key) \
            .findout_searchresult(text) \
            .goto_stock_tab(tab_title) \
            .get_price(text)

        assert_that(stock_price, close_to(price, price *0.1))

    def test_search2(self):
        search_key = "alibaba"
        text = "BABA"
        title = "股票"

        stock_price = self.mainpage.click_search() \
            .find_input_search(search_key) \
            .findout_searchresult(text) \
            .goto_stock_tab(title) \
            .get_price(text)

        assert_that(stock_price, close_to(110, 110 * 0.1))
