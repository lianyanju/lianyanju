# range 对象是一个迭代器对象，用来产生指定范围的数字序列。
# 格式为： range(start, end [,step])

# 生成的数值序列从start 开始到 end结束(不包含 end)。【前闭后开】
# 若没有填写start，则默认从 0 开始。step是可选的步长，默认为 1。
# 如下是几种典型示例：

# for i in range(10) 产生序列：0 1 2 3 4 5 6 7 8 9
#
# for i in range(3,10) 产生序列：3 4 5 6 7 8 9
#
# for i in range(3,10,2) 产生序列：3 5 7 9


print([i*3 for i in range(1,4)])