from typing import List
from typing import TYPE_CHECKING

import pytest
import yaml

if TYPE_CHECKING:
    from _pytest.config import Config
    from _pytest.main import Session
    from _pytest.nodes import Item

"""实现hook相当于写了一个小的插件"""


# 插件1：实现用例编码 + 用例执行顺序
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    # 改变属性编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # name 用例的名字
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # nodeid 就是测试用例路径

    # 改变用例执行顺序
    items.reverse()


"""  hook函数的使用不需要手动调用，【不需】要引用方把hook名字当成参数传递"""


# hook函数，添加命令行参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("lianyanju")
    mygroup.addoption("--env",
                      default='test',
                      dest='dev',
                      help='设置接口自动化测试默认的环境'
                      )


""" 定义成fixture，应用时 把cmdoption 名字当成参数传递"""


# 获取设置的命令行参数,并返回不同环境对应的测试数据
@pytest.fixture(scope='session')
def cmdoption(config):

    datapath = None
    myenv = config.getoption("--env", default='test')
    # myenv = request.config.getoption("--env", default='test')
    print(f"myenv的值是：{myenv}")

    if myenv == 'test':
        datapath = "datas/test/data.yaml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yaml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
