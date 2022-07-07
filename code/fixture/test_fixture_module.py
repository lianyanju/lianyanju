import pytest


# 作用域：module是在模块之前执行， 模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")

    yield

    print("执行teardown !")
    print("最后关闭浏览器")
    return 2

def test_search2(open):
    print("open====", open)
    print("当前测试用例：test_search2")
    print("")
    pass


def test_search3(open):
    print("open====", open)
    print("当前测试用例：test_search3")
    print("")
    pass


def test_search4():
    print("open====", open)
    print("当前测试用例：test_search4")
    pass

"""
1： 当 scope='module' 时，在当前 .py 脚本里面所有的用例开始前只执行一次
2： scope="module" 与 yield 结合，相当于 setup_module 和 teardown_module 方法。
3： 整个模块运行之前调用了 open()方法中 yield 前面的打印输出“打开浏览器”,
    整个运行之后调用了 yield 后面的打印语句“执行 teardown !”与“关闭浏览器”。
    
    yield 来唤醒 teardown 的执行，如果用例出现异常，
   不影响 yield 后面的 teardown 执行。
"""