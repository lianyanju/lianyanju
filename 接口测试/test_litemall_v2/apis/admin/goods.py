import requests

from 接口测试.test_litemall_v2.apis.baseapi import BaseApi


class Goods(BaseApi):

    #货物上架
    def create_goods(self, goods_data):
        path = "/admin/goods/create"
        respose_json = self.send("post", path, json=goods_data)
        return  respose_json


    def get_goods_list(self,goods_name,order="desc",sort="add_time"):
        path = "/admin/goods/list"
        goods_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        respose_json = self.send("get", path, params=goods_data)

        return respose_json

    def get_goods_detail(self, goods_id):
        path = "/admin/goods/detail"

        respose_json = self.send("get", path, params={"id": goods_id})

        return respose_json

    def delete_goods(self, goods_id):
        path = "/admin/goods/delete"
        res = self.send("post", path, json={"id": goods_id})
        return res

    def delete_by_id(self, goods_id):
        path = "/admin/goods/delete"
        res = self.send("post", path, json={"id": goods_id})
        return res
