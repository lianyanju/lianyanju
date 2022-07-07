"""
目的：通过环境变量切换使用不同的配置文件
"""
import os

import requests
import yaml


# 设置临时环境变量
# windows set interface_env=test
# windows下如果使用powershell，需要使用  $env:interface_env="dev"  命令设置环境变量

# mac export interface_env=test

class TestMulitiEnv:

    def setup_class(self, ):
        print("----------3---------------")
        # 从yaml文件读取数据
        # 第一种方式： 从环境变量读取名称为interface_env的配置环境
        # 前提：运行之前设置临时环境变量： 命令行执行：export interface_env=test
        path_env = os.getenv("interface_env", default="test")
        print(f"path_env========{path_env}")

        # 读取对应的文件内容
        env = yaml.safe_load(open(f"{path_env}.yaml", encoding="utf-8"))

        self.base_url = env["base_url"]

        # ==== 执行方法：
        # 1： 命令行 执行用例pytest .\test_muliti_env.py
        # 2： ide运行文件


    # 验证是否是开发环境
    def test_devenv(self):
        print("-----------4---------------")
        path = "get"
        r = requests.get(self.base_url + path)
        assert r.json()["headers"]["Host"] == 'httpbin.ceshiren.com'

    # 验证是否是测试环境
    def test_testenv(self):
        print("-----------5---------------")
        path = "get"
        r = requests.get(self.base_url + path)
        assert r.json()["headers"]["Host"] == 'httpbin.org'
