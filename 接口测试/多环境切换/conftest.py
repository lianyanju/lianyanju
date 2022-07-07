"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

global_env = {}


# hook 函数，是添加命令行参数使用
def pytest_addoption(parser):
    print("-----------1---------------")
    # group 将下面所有的 option都展示在这个group下。
    mygroup = parser.getgroup("hogwarts")
    # 注册一个命令行选项
    mygroup.addoption("--env",
                      default='test', # 参数的默认值
                      dest='env',# 存储的变量
                      help='设置接口自动化测试默认的环境' # 参数的描述信息
                      )


# 获取设置的命令行参数
def pytest_configure(config):
    print("-----------2--------------")
    default_ev = config.getoption("--env")
    tmp = {"env": default_ev}
    global_env.update(tmp)
