import pytest

# 定义了登录的fixture，尽量避免以test_开头
"""
@pytest.fixture
def fixture_name():
    setup 操作
    yield 返回值
    teardown 操作
"""


@pytest.fixture(scope="class")
def login():
    # setup 操作
    print("完成登录操作")

    token = "lilliputian"
    username = 'hogwarts'

    yield token, username
    # yield关键字相当于return，后面不跟 表示返回None
    # yield这一行执行完，就进入测试用例里面 测试用例执行完毕，再回到这里继续往下执行

    # teardown 操作
    print("完成登出操作")


def test_search(login):
    token, username = login
    print(f"token：{token} , name : {username}")
    print("搜索")


def test_cart(login):
    token, username = login
    print(f"token：{token} , name : {username}")
    print("购物车")
