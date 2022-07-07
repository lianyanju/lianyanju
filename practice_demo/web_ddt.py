import unittest

from test_ddt import *

import requests



s = requests.Session()

args_list = [
    ({"json": {"username": "sanmu", "password": "123456"}}, 200),
    ({"json": {"username": "sanmu", "password": "123456"}}, 400),
    ({"json": {"username": "sanmu", "password": "123456"}}, 422)
]


@ddt
class MyTest(unittest.TestCase):
    base_url = "http://api.tttt.one"

    def full_url(self, uri):
        return self.base_url + uri

    # def test_login_with_json(self, data, code):
    #     for data,code in args_list:
    #         with self.subTest(f"{code}"):
    #             resp = s.request("POST", self.full_url(""), **data)
    #             self.assertEqual(resp.status_code, code)
    # 下面这个就代替了 上面的方法

    @data(*args_list)
    @unpack
    def test_login_with_json(self, param, code):
        resp = s.request("POST", self.full_url(""), **param)
        self.assertEqual(resp.status_code, code)




if __name__ == '__main__':
    unittest.main()