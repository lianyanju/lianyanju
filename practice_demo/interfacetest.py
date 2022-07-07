import requests

res1 = requests.get("http://*")
res2 = requests.get("http://*")
res8 = requests.request("get","http://*")


s = requests.session()

res3 = s.get("http://*")
res4 = s.get("http://*")


# res1 和 res2 创建的都是一次性会话，会各占用一个端口， 用完就断开链接
# 但是：由于tcp三次握手和四次挥手的原因，在很长一段时间内 释放的端口还是不能再次使用
# 由于一个电脑的端口数量是有限的，所以尤其接口测试 非常不建议用上面的写法
# 注意：res2和res8是一样的 只不过res2的最终实现还是调用res8


# 而res3和res4是【公用】提前创建好的一个会话 ，只占用一个端口
# 好处2：省去了每次建立tcp连接的开销
#