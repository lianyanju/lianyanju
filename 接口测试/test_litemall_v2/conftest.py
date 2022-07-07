import os.path
import time

import pytest


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
