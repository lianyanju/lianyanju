import json
import random
import unittest

import requests


class APIClient:
    """
     和API相关的一切内容
    """
    pass

    def __init__(self):
        self.session = requests.Session()

    def request(self, *args, **kwargs):
        return requests.Response

    def user_sign_up(self, password="", email="", **kwargs):
        """
           注册接口
           :param password
           :param email
           :param kwargs

           :return
        """
        method = "post"
        url = "http://hdshkfsd/login/sign_up"
        body = {"password": password, "username": email}
        kwargs["json"] = body
        return self.request(method, url, **kwargs)

    def user_login(self, password="", email="",**kwargs):
        """
          登陆接口
          :param password
          :param email
          :param kwargs

          :return
         """
        method = "post"
        url = "http://hdshkfsd/login"
        body = {"username": email, "password": password}

        kwargs["json"] = body
        return self.session.request(method, url, kwargs)


class UserAPITest(unittest.TestCase):
    """
        和测试用例相关
       """

    api = APIClient()

    def _create_user(self, email, password):
        pass

    def setUp(self):
        self.test_users = []

    def tearDown(self) -> None:
        for email in self.test_users:
            try:
                user = User.get(email=email)
                # 这里的User 是 有peewee通过数据库中已经存在
                # 表来生产的对应ORM关系类

                user.delete_instance()
            except User.ç:
                print(f"email:{email} email")

    def test_user_login(self):
        # 1：创建测试数据
        email = f"sanmu{random.randint(1, 9999)}@qq.com"
        password = "123456"

        # 2:创建用户
        self._create_user(email=email, password=password)

        # 3:调用登陆接口
        resp = self.api.user_login(email=email, password=password)

        self.assertEqual(resp.status_code, 200)

        self.assertIn("access_token", resp.text)

    def test_user_sign_up(self):

        email = f"sanmu{random.randint(1, 9999)}@qq.com"
        password = "123456"
        self.test_users.append(email)  # 测试用户记录下来

        resp = self.api.user_sign_up(email, password)

        self.assertEqual(resp.status_code, 200, resp.json())  # 断言接口请求成功

        user_by_api = resp.json()
        user_by_db = User.get(email=email)
        self.assertEqual(user_by_db.id, user_by_api["id"])  # 断言数据入库，接口响应正常


if __name__ == '__main__':
    unittest.main()
