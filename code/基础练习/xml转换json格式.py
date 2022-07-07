"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests
import xmltodict


def test_xml_to_dict():
    res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")

    # 注意，不是直接打印r 而是打印 r 的 text 属性,因为res是一个Response对象
    print(res.text)
    # # 转换成python标准的dict格式
    # res_dict = xmltodict.parse(res.text)
    # print(res_dict)