import unittest
from time import sleep

from selenium import webdriver
from ddt import *

#good 参数化的ddt


@ddt
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.baidu.com")
        # cls.driver.maximize_window

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def search(self, search_key):
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(5)

    @data(
        ("case1", "selenium"),
        ("case2", "python")
    )
    @unpack
    def test_search1(self, name, search_key):
        print("第一组测试用例：", name)
        self.search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @data(
        ["case1", "selenium"],
        ["case2", "python"]
    )
    @unpack
    def test_search2(self, name, search_key):
        print("第二组测试用例：", name)
        self.search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @data(
        {"key": "selenium"},
        {"key": "python"}
    )
    @unpack
    def test_search3(self, key):
        print("第三组测试用例：", key)
        self.search(key)
        self.assertEqual(self.driver.title, key + "_百度搜索")

    if __name__ == '__main__':
        unittest.main()
