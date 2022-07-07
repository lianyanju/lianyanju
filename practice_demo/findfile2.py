import unittest


# 第一步先创建子类，继承测试框架
class mytest(unittest.TestCase):

    # 每次执行一个函数都要先执行这个函数，有几个函数就被调用几次，与放的位置无关，随便放到哪里都会先执行这个函数
    def setUp(self):
        print("\n我是 setUp")
        from common import add
        self.add = add  # 把导入的add赋值给self身体

    def tearDown(self):
        print("我是 tearDown")

    # 第二部 定义测试用例
    def test_first(self):
        _a = 3 + 5
        _b = self.add(3, 5)
        self.assertEqual(_a, _b)

    def test_second(self):
        _a = 3 + 5
        _b = self.add(3, 7)
        self.assertEqual(_a, _b)

    def test_third(self):
        _a = 3 + 5
        _b = self.add(3, 8)
        self.assertEqual(_a, _b)


# 第三步：添加总入口
if __name__ == '__main__':
    # unittest.main()  #主方法 程序入口
    unittest.main(verbosity=2)  # 技巧，点击进入mian函数中，里面有很多参数，更有用
