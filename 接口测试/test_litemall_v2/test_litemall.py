"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import json

import pytest
import requests

from 接口测试.test_litemall_v1.log_utils import logger


class TestLitemall:

    def setup_class(self):
        # 1. 管理端登录接口
        url = "http://litemall.hogwarts.ceshiren.com/admin/auth/login"
        user_data = {"username": "admin123", "password": "admin123", "code": ""}
        r = requests.post(url, json=user_data)
        self.token = r.json()["data"]["token"]
        # 问题： 没有执行test_get_admin_token这个方法，所以self.token 就不会被声明就会报错'TestLitemall' object has no attribute 'token'
        # 解决， self.token 的声明一定要在test_add_goods方法执行之前完成，可以使用setup_class 提前完成变量的声明
        # 2. 用户端登录接口
        url = "http://litemall.hogwarts.ceshiren.com/wx/auth/login"
        client_data = {"username": "user123", "password": "user123"}
        r = requests.post(url, json=client_data)
        self.client_token = r.json()["data"]["token"]
    # ======= 数据清理，建议使用delete接口不要直接删表中的数据
    def teardown(self):
        print("4444444444444")
        url = "http://litemall.hogwarts.ceshiren.com/admin/goods/delete"
        r = requests.post(url, json={"id":self.goods_id}, headers={"X-Litemall-Admin-Token": self.token})
        logger.debug(f"删除商品的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

    # 上架商品接口调试
    # ====问题2： goods_name 不能重复，所以需要添加参数化
    @pytest.mark.parametrize("goods_name", ["ADcarry12", "ADcarry13"])
    def test_add_goods(self, goods_name):
        # 3. 上架商品接口
        url = "http://litemall.hogwarts.ceshiren.com/admin/goods/create"
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "66", "number": "66", "url": ""}],
            "attributes": []}
        r = requests.post(url, json=goods_data, headers={"X-Litemall-Admin-Token": self.token})
        logger.debug(f"上架商品接口接口的相应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

        # 4. 获取商品列表
        goods_list_url = "http://litemall.hogwarts.ceshiren.com/admin/goods/list"
        goods_data = {
            "name": goods_name,
            "order": "desc",
            "sort": "add_time"
        }
        r = requests.get(goods_list_url, params=goods_data,
                         headers={"X-Litemall-Admin-Token": self.token})
        self.goods_id = r.json()["data"]["list"][0]["id"]
        logger.debug(f"获取商品列表接口的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

        # 5.获取商品详情接口=========
        goods_detail_url = "http://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        r = requests.get(goods_detail_url, params={"id": self.goods_id},
                         headers={"X-Litemall-Admin-Token": self.token}                         )
        product_id = r.json()["data"]["products"][0]["id"]
        logger.debug(f"获取商品详情接口的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

        # 6. 添加购物车接口
        url = "http://litemall.hogwarts.ceshiren.com/wx/cart/add"
        cart_data = {"goodsId": self.goods_id, "number": 1, "productId": product_id}
        r = requests.post(url, json=cart_data, headers={"X-Litemall-Token": self.client_token})
        res = r.json()
        logger.info(f"添加购物车接口响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

        assert res["errmsg"] == "成功"



    def test_m(self):
        var = 1 / 0


