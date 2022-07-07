import unittest
from time import sleep
from selenium import webdriver
from ddt import *


# good file文件的ddt


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

    @file_data('ddt_data.json')
    def test_search1(self, search_key):
        print("第一组测试用例：", search_key)
        self.search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @file_data('ddt_data_yml.yaml')
    def test_search2(self, case):
        print("casecase：", case)
        search_key = case[0]["search_key"]
        print("第二组测试用例：", search_key)
        self.search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")


if __name__ == '__main__':
    unittest.main(verbosity=2)
