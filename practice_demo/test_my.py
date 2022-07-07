import unittest


def setUpModule() -> None:
    print("\n我是 setModule")
    from practice_demo.common import add
    test2.add = add  # 把导入的add赋值给self身体


class test2(unittest.TestCase):

    def test_first(self):
        _a = 3 + 5
        _b = test2.add(3, 5)
        self.assertEqual(_a, _b)

class cls2(test2):
    def test_first2(self):
        pass


if __name__ == '__main__':
    # unittest.main()  #主方法 程序入口
    unittest.main(verbosity=2)  # 技巧，点击进入mian函数中，里面有很多参数，更有用
