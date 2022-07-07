"""
装饰器
函数在开始执行与结束执行的时候分别打印提示信息
"""

# def hogwarts():
#     print("霍格沃兹测试学社")
#
# def hogwarts2():
#     print("霍格沃兹测试学社2部")

# # 第二步优化，把中间的执行函数，使用参数代替
# def function_tips(func):
#     print("函数开始执行")
#     # 不再是写死的任何的一个函数，而是任意外部传入的函数对象
#     func()
#     print("函数结束执行")
#
# # 需要传入一个函数对象
# function_tips(hogwarts2)

# 使用装饰器实现函数在开始执行与结束执行的时候分别打印提示信息

# 第一步，定义两个函数，一个内函数，一个外函数
# 第五步，在装饰器执行过程中，会自动传入一个参数,参数就是被装饰函数的函数对象
# def timer(func):
#     def inner():

#         # 第二步，在内函数添加装饰器的逻辑
#         print("函数开始执行")
#         func() #第六步 添加被装饰函数的执行步骤
#         print("函数结束执行")

#     # 第三步 把内函数的函数对象return 出去
#     return inner
#
# # 第四步，装饰器的使用
# @timer
# def hogwarts():
#     print("霍格沃兹测试学社")
#
# @timer
# def hogwarts2():
#     print("霍格沃兹测试学社二部")
#
# hogwarts2()


# 三步走： 1. 定义一个外函数，外函数有一个形参，接受被装饰的函数对象
# 2. 定义一个内函数，内函数内调用传入函数
# 3. 定义外函数的返回值,外函数返回值固定格式为内函数对象
# 实现一个计时器的装饰器，计算函数执行时间

import datetime
def timer(func):
    # 如果被装饰函数有参数，那么需要在内函数加形参以及，在函数参数调佣的时候添加参数信息
    # 如果写死一个参数，但是无法确定被装饰函数的参数数量，这种写法就不行，会报错
    # 解决方案： 把两个地方的参数全部换成不定长参数
    def inner(*args, **kwargs):
        # 获取当前时间
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"函数的执行时间{end_time-start_time}")
    return inner

@timer
def hogwarts(name):
    print("霍格沃兹测试学社", name)

@timer
def hogwarts2(name, age, gender):
    print("霍格沃兹测试学社二部")
    print(name)
    print(age)
    print(gender)


hogwarts("harry")
hogwarts2("罗恩", 11, "男生")

