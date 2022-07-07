"""
__author__ = 'hogwarts_xixi'
"""
import pytest


@pytest.fixture(params=[["selenium",123],["appium",123456]])
def login(request):# 这里的request是固定的 内置的
    print(f"用户名：{request.param}")
    return request.param

def test_demo1(login):
    data = login
    print(f"demo1 case: 数据为： {data}")