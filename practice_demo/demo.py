import unittest


def add(a, b):
    return a + b


# 第一步先创建子类，继承测试框架
class mytest(unittest.TestCase):

    # 第二部 定义测试用例
    def test_first(self):
        _a = 3 + 5
        _b = add(3, 5)
        self.assertEqual(_a, _b)


# 第三步：添加总入口
if __name__ == '__main__':
    unittest.main()  # 主方法 程序入口
    # unittest.main(verbosity=2)  技巧，点击进入mian函数中，里面有很多参数，更有用
