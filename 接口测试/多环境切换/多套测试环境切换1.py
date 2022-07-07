"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

import requests

class TestMulitiEnv:
    def setup_class(self,):

        # 目的 ： 在接口用例中只指定path，不指定url
        self.base_url = 'http://httpbin.ceshiren.com/'

    # 验证是否是开发环境
    def test_devenv(self):
        path = "get"
        r = requests.get(self.base_url+path)
        # 假设 httpbin.ceshiren.com 是开发环境，那么就是断言，当前i请求是否是
        # 向开发环境发起的
        assert r.json()["headers"]["Host"] == 'httpbin.ceshiren.com'

    # 验证是否是测试环境
    def test_testenv(self):
        path = "get"
        r = requests.get(self.base_url + path)
        assert r.json()["headers"]["Host"] == 'httpbin.org'


