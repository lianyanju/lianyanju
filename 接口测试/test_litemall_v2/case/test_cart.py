import json

import pytest
import requests

from 接口测试.test_litemall_v2.apis.admin.goods import Goods
from 接口测试.test_litemall_v2.apis.mallclient.carts import Carts



class TestCarts:
    def setup_class(self):

        #i实例化业务apis Goods
        self.goods=Goods("admin")
        self.carts = Carts("client")


    """
    添加添加购物车测试------
      上架商品接口
      获取商品列表
      获取商品详情接口
      添加购物车接口
    """
    @pytest.mark.parametrize("goods_name", ["ADcarry12", "ADcarry13"])
    def test_addcart(self, goods_name):
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "66", "number": "66", "url": ""}],
            "attributes": []}
        self.goods.create_goods(goods_data)

        goods_lists = self.goods.get_goods_list(goods_name)
        goods_id = goods_lists["data"]["list"][0]["id"]

        goods_info= self.goods.get_goods_detail(goods_id)
        product_id = goods_info["data"]["products"][0]["id"]

        self.carts.add_cart(goods_id, product_id)

        # 为什么要把delete 放在用例中
        # 1. 调用方法，使用方便
        # 2. 测试类当中的每个测试方法并非都会添加goods 数据，如果部分用例不添加，那么相当于这个步骤，不能在每个测试用例执行完成之后执行
        # 只能在当个用例执行完成之后执行
        self.goods.delete_by_id(goods_id)


