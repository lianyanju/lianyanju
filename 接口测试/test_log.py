import logging
import unittest

file_handler = logging.FileHandler("log/my_test.log", encoding="utf-8", mode="w")
formatter = logging.Formatter("%(levelname)-8s [%(name)s]  %(asctime)s: %(message)s")
file_handler.setFormatter(formatter)

logger = logging.getLogger("TestCase")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)


# 1:如果需要在unittest中记录接口请求和返回日志 【但又因为该框架不支持，so，需要我们自己封装一下】
# 框架，是一个非常抽象的东西
# 首先要明白
# 测试方法（test_*）,由谁来调用呢：由unittest中的run（）调用
# so，我们要重写改函数来实现请求和响应的日志打印需求

class BaseTestCase(unittest.TestCase):

    def run(self, result=None):
        # result，默认就是TestResult
        logger.info("~~ \n")
        logger.info(f"开始执行测试用例了 (TestCase: {self.id()})")

        result = super().run(result)
        # result是本次测试所有用例的测试结果

        logger.info(f"测试用例执行结束了 (TestCase: {self.id()})")

        if result:
            # 如果失败，记录失败的原因

            # 前提知道result有哪些属性，比如有failures，errors，其次知道他们的格式
            # result.errors = [
            #     (用例对象,失败原因),
            #     (用例对象, 失败原因)
            # ]

            # self 就是用例本身
            for case, info in result.failures:

                if self is case:
                    logger.warning(f"测试失败 (TestCase: {self.id()})")
                    logger.warning(f"{info})")
                    return result

            for case, info in result.errors:
                if case is self:
                    logger.error(f"测试出错 (TestCase: {self.id()})")
                    logger.error(f"{info})")
                    return result

            for case, info in result.skipped:
                if case is self:
                    logger.error(f"测试跳过 (TestCase: {self.id()})")
                    logger.error(f"{info})")
                    return result

        logger.info(f"测试通过 (TestCase: {self.id()})")
        return result


class TestCase(BaseTestCase):
    def setUp(self) -> None:
        super(TestCase, self).setUp()

    def test_pass(self):
        logger.info("你好  我是  艳举")

    def test_fail(self):
        self.fail()

    def test_error(self):
        var = 1 / 0

    @unittest.skip("skip")
    def test_skip(self):
        pass

    @unittest.expectedFailure
    def test_xfail(self):
        assert False


if __name__ == '__main__':
    unittest.main()
