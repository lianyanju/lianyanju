a = print   #把print函数当成一个值赋值给变量a
a("lllll") #a就可以当成print使用

def get_print():
    return print

get_print()("pppp")

#等价于
b = get_print()
b("pp7777pp")
