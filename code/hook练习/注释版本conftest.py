"""
1： Extental Libraries---》 site-packages--〉——pytest--》hookspec.py
    里面定义了各种hook ，你可以在conftest里面实现这些hook
    这些hook贯穿着整个测试用例生命周期

    hookspec里面copy到conftest

"""
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


# 插件2：定义一个命令行参数
# ps：pytest_addoption 名字是固定的不可以改动
#  验证方式：
#  1：右键该文件---open in termial
#  2：输入命令： python3 -m pytest --help  就会发现分组里面有hogwarts 以及下面--env
#  3：或者输入命令：python3 -m pytest --help |grep lianyanju  能过滤出lianyanju分组
#  注意不需要执行该代码  在你执行命令时 会自动执行这一个文件！！！
def pytest_addoption(parser): #parser是固定的

    mygroup = parser.getgroup("lianyanju")  # 如果parser.getgroup没有返回结果，就新建了，如果返回了就在返回的基础之上新增
    mygroup.addoption("--env",
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量
                      help='设置接口自动化测试默认的环境'  # 参数的描述信息
                      )


# 获取设置的命令行参数
# ps：cmdoption 名字可以随便起
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = "datas/test/data.yml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv,datas