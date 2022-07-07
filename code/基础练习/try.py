# rdata = {"k1":"v1", "k2":"v2"}
# print(rdata)
#     # print(f"返回数据为{json.dumps(rdata,indent = 2)}")
#     # print(f"返回数据为{json.dumps(rdata)}")

kwargs= {"k1":"v1",'header':"000"}

if kwargs.get("header"):  # dict.get(key) 和dict(key) 一样，不过dict(key)没这个key时会报错
    # kwargs["header"]["X-Litemall-Admin-Token"] = "token"
    kwargs["header"].update({"X-Litemall-Admin-Token": "token"})
else:  # None
    kwargs["header"] = {"X-Litemall-Admin-Token": "token"}
    print(kwargs)