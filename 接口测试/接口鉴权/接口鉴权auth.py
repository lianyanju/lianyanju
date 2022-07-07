"""
   这是一种简单的身份认证，它是通过http的authorization请求头中，
   每次请求：携带经过base64加密的用户名和密码而实现的一种认证。
   base64（username + password）

    服务端接收用户名和密码之后会解密其内容，从而获取真实用户名和密码，之后再去同步数据库中的用户名和密码

    缺点：无论是java还是pyhton都有各种解base64的库   即 不安全
"""
import requests
from requests.auth import HTTPBasicAuth


class TestTokenVerify:
    def setup_class(self):
        self.proxy = {
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        }

    def test_basic_auth(self):

        # 两种写法：第一种auth=HTTPBasicAuth("ad", "123")
        # r = requests.get("https://httpbin.ceshiren.com/basic-auth/ad/123",
        #                  auth=HTTPBasicAuth("ad", "123"), proxies=self.proxy, verify=False)

        # 两种写法：第二种auth=("ad", "123")
        r = requests.get("https://httpbin.ceshiren.com/basic-auth/ad/123",
                         auth=("ad", "123"), proxies=self.proxy, verify=False)
        print(r.json())