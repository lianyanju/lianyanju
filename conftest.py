# import time
#
# import pytest
#
#
# @pytest.fixture(scope="session", autouse=True)
# def manage_logs(request):
#     now = time.strftime("%Y-%m-%d %H-%M-%S")
#     log_name = './log/' + now + '.logs'
#
#     request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
#
#
# @pytest.fixture()
# def login():
#     print("")
#     print('输入用户名，密码。完成登录')
#
#     yield
#     print('退出')
#
#
# @pytest.fixture()
# def data():
#     print('---我是data函数-----')
#
# @pytest.fixture()
# def buCuo():
#     print('---我是buCuo函数-----')


# 收集完测试用例 之后被调用的hook函数
# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     print(items)
#     # name 用例的名字
#     # nodeid 就是测试用例路径
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#     items.reverse()