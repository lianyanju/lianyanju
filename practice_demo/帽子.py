from dataclasses import dataclass

# @dataclass是一个装饰器，用于自动生成一些special method并添加到类中
@dataclass
class man:
    name: str
    age: int

a_man = man(name="ni hao", age=29)
print(f"{a_man.name}的年龄是{a_man.age}")

# 在这个例子中， name 和 age 都将包含在添加的 __init__() 方法中，它们将被定义为:
# def __init__(self, name: str, b: age = 0):
# 相当于自己不用重写__init__构造函数了
