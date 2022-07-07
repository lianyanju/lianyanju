"""
   这是一种简单的身份认证，产品中其实越来越少这种方式 而是token，因为不安全
   1：第一次获取cookie之后，响应头里面会有set-cookie 可以从这里获取cookie 且 自动为后续的请求头中添加cookie信息

   2： 后续每次请求：的请求头中都有cookie为key的数据
     ps：注意以放在要用同一个session连接请求 ，不然 请求的cookie中不能共享之前set设置的cookie


"""
import requests


class TestCookieVerify:
    def setup_class(self):
        #目的：可以通过抓包代理工具 查看 请求和响应细节
        #前提是 启动代理 工具


        self.proxy = {
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        }


    def test_cookies(self):
        """
        在有确定的cookies信息的情况下，可以直接使用cookies参数
        :return:
        """
        r  = requests.get("https://httpbin.ceshiren.com/cookies", cookies={"hogwarts": "ad"})
        print(r.json())

    def test_cookies_with_out_session(self):
        # 1. 获取cookie
        # 2. set cookie 设置cookie
        # 3. 再次获取cookie，查看是否设置成功
        r1 = requests.get("https://httpbin.ceshiren.com/cookies", headers={"count":"1"},  proxies=self.proxy, verify=False)
        print(f"第1次的响应值为{r1.json()}")
        r2 = requests.get("https://httpbin.ceshiren.com/cookies/set/username/123456", headers={"count":"2"}, proxies=self.proxy, verify=False)
        print(f"第2次的响应值为{r2.json()}")
        r3 = requests.get("https://httpbin.ceshiren.com/cookies",headers={"count":"3"}, proxies=self.proxy, verify=False)
        print(f"第3次的响应值为{r3.json()}")

    def test_cookies_session(self):

        req = requests.session()
        r2 = req.get("https://httpbin.ceshiren.com/cookies/set/username/123456", headers={"count": "1"},
                          proxies=self.proxy, verify=False)
        print(f"第1次的响应值为{r2.json()}")
        r3 = req.get("https://httpbin.ceshiren.com/cookies", headers={"count": "2"}, proxies=self.proxy,
                          verify=False)
        print(f"第2次的响应值为{r3.json()}")
        r4 = req.get("https://httpbin.ceshiren.com/cookies", headers={"count": "3"}, proxies=self.proxy,
                     verify=False)
        print(f"第3次的响应值为{r4.json()}")
