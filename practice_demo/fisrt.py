def add(a=1, b=2, **kwargs):  # 用两个表示关键字参数
    # print("c :", c)
    print("kwargs :", kwargs)


    return a + b


result = add(b=3, c=1, d=1, a=4)  # 指定关键字参数，跟位置没有关系
result1 = "Eric "
print("add(3)    =", result1)
print("一二班    =", result1)
