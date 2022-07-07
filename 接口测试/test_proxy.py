import requests

# 定义一个代理的 配置信息,
# key值为【协议】，
# value 为代理工具的配置,
proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# 通过proxies 传递代理配置
data = {"a":1}
url = "https://httpbin.testing-studio.com/post"
requests.post(url=url, proxies=proxy, json=data,  verify=False)

#运行代码之前开启代理工具：charles