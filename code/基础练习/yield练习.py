"""
yield 属于 pytest 不是python的

1：yield关键字

2：它不是单独存在，要写在fixtrue标记的搭配使用。

3：作用：yield操作退出清理数据 【唤醒teardown】

4：测试用例异常不影响yield后续的执行

5：如果在setup就异常【即yield前面的代码】，那么是不会去执行yield后面的teardown内容。

当fixture参数scope=”module”，module作用是整个.py文件都会生效（ 整个文件只会执行一次），
用例调用时，参数写上函数名称就行。


神帖子：https://blog.csdn.net/hyq413950612/article/details/120760752

"""

import pytest

@pytest.fixture(scope="module")
def login():
    print(u"登录成功")
    yield
    print(u"用例执行完成，收尾")

def test_one(login):
    print(u'操作1')

def test_two(login):
    print(u'操作2')

def test_three(login):
    print(u'操作3')

if __name__ == "__main__":
    pytest.main(["-s", "test_yield_module.py"])
