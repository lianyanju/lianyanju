#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# 可以理解为夹具

@pytest.fixture()
def login():
    print("这是个登录方法")
    return 'tom', '123'


@pytest.fixture()
def operate():
    print("登录后逻辑的操作")


# 如下是几个测试用例
def test_case1(login, operate):
    print("当前测试用例：test_case1，需要登录")
    print("")


def test_case2():
    print("当前测试用例：test_case2，不需要登录")
    print("")


def test_case3(login):
    print(login)  # 打印的是 函数的返回值
    print("当前测试用例：test_case1，需要登录")
    print("")
