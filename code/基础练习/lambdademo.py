# lambda 表达式可以理解为一个函数
# lambda 后面的参数【可以】省略，
# "：" 不可以省略，
# "："后面也不可以省略，

# demo1
# result = lambda r: 2 * r     
# print(f"{result(3)}")

# demo2
# result = lambda : 2
# print(f"{result()}")

# ✨✨日常开发常用 ：对获取到的信息进行排序
lists_info = [
     ("java书本","77"),
     ("测试书本","107"),
     ("python书本","33")]

print(lists_info)
lists_info.sort(key=lambda x:x[1])

print(lists_info)

#这里的x是指列表中每一个元素（元祖）
#lambda x:x[1] 返回了列表中每个元祖中的第二个元素