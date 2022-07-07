import os.path
import time

import pytest

"""
 注意这个文件 一个项目下可以有多个
 放在不同package下作用域不一样
 
 比如：放在xueqiu_po_demo 下就会运行xueqiu_po_demo下的文件 
 
"""

# request.config.rootdir: 用于获取项目的跟目录
def get_root_dir(request):
    root_dir = request.config.rootdir
    return root_dir


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    log_name = "logs/" + now + '.log'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(os.path.join(get_root_dir(request), log_name))
