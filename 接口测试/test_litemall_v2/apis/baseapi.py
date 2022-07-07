import json
import logging

import requests



class BaseApi:

    def __init__(self, role=None):
        self.base_url = "http://litemall.hogwarts.ceshiren.com"
        # 获取对应的角色信息
        if role:
            self.role = role



    def __set_header__(self, req_kwargs):
        """
              # 问题： 除登录接口之外，基本每一个接口，都需要另外去设置token
              # 解决方案：
                  1. 在发起接口请求之前，就获取token信息
                  2. 获取token信息之后，塞入到请求信息之中
                      1. 除了method 和url 之外，所有的其他信息，包括header params 等等的其他参数，都会塞入至kwargs 不定长参数中
                      cart_api -> send-> 获取kwargs -> 在kwargs 中 塞入header（鉴权）信息
              # 问题2: 如果有两个token存在怎么办？
              # 1. 不同的角色有不同的token信息

              :return:
          """

        # 1. 【管理端】登录接口
        admin_path = "/admin/auth/login"
        user_data = {"username": "admin123", "password": "admin123", "code": ""}
        admin_res = requests.request("post", self.base_url+admin_path, json=user_data)
        self.token = {"X-Litemall-Admin-Token", admin_res.json()["data"]["token"]}

        # 2. 【用户端】登录接口
        wx_path = "/wx/auth/login"
        client_data = {"username": "user123", "password": "user123"}
        wx_res = requests.request("post",  self.base_url+wx_path, json=client_data)
        self.client_token = {"X-Litemall-Token", wx_res.json()["data"]["token"]}

        if self.role == "admin":

            self.final_token = self.token
        else:
            self.final_token = self.client_token

        if req_kwargs.get("header"):
            req_kwargs["header"].update(self.final_token)
        else:
            req_kwargs["header"] = self.final_token

        return req_kwargs

    """
    # 问题1： 接口里面直接使用了requests
    # 解决方案： 在base_api中添加公共的send方法

    # 问题2：大量重复的base_url
    # 解决方案，在构造函数，实例化base_url，并且在send方法，就直接做拼接，
    这样子类的方法，就无需重复编写self.base_url
    
    # 优化3： token 的获取也放到了基类basepi的构造函数里面




    """
    def send(self, method, url, **kwargs):

        kw_args = self.__set_header__(kwargs)
        res = requests.request(method, self.base_url + url,  **kw_args)
        logging.debug(f"url为：{url},接口返回信息为{json.dumps(res.json(), indent=2, ensure_ascii=False)}")
        return res.json()