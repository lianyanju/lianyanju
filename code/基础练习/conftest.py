# 收集完测试用例 之后被调用的hook函数

from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _pytest.config import Config
    from _pytest.main import Session
    from _pytest.nodes import Item



def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    # 改变属性编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # name 用例的名字
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # nodeid 就是测试用例路径

    # 改变用例执行顺序
    items.reverse()
