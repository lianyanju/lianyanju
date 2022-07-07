"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests
import xmltodict
from requests import Response


def test_response_to_dict():
    res = requests.get("https://httpbin.ceshiren.com/get")

    final_res = reponse_to_dict(res)
    print(final_res)

    # 断言响应值是否为dict类型的格式
    assert isinstance(final_res, dict)


def reponse_to_dict(response: Response):
    res_text = response.text

    # 判断响应文本信息是否以 <?xml开头
    if res_text.startswith("<?xml"):
        final_dict = xmltodict.parse(res_text)

    elif res_text.startswith("<!DOCTYPE html>"):
        final_dict = "html"

    # 如果是json 则返回json格式
    else:
        final_dict = response.json()

    return final_dict