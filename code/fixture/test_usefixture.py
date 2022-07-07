import pytest


# login函数定义在先在conftest.py中
@pytest.mark.usefixtures('login')
class Test_01:

    def test_01(self):
        print('---用例01---')

    def test_02(self):
        print('---用例02---')

    def test_03(self):
        print('---用例03---')


"""
    看到装饰器的参数就能晓得，usefixtures 和 fixture 要配合使用的。
    下面使用例子演示一下：
    先在conftest.py配置fixture。
    再定义使用fixture的程序。
    
    通过执行结果可以发现，【通过使用usefixture方法后，测试类包含的每个用例都会执行前置和后置内容。】
    就不用为改模块中每一个测试用例进行登陆操作了


"""
