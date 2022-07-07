

from 接口测试.test_litemall_v2.apis.baseapi import BaseApi


class Carts(BaseApi):

    def add_cart(self, goods_id, product_id):
        # 6. 添加购物车接口
        url = "/wx/cart/add"
        cart_data = {"goodsId": goods_id, "number": 1, "productId": product_id}
        res = self.send("post",url, json=cart_data)
        return res
