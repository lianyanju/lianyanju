


# 141个收藏
# https://blog.csdn.net/wls666/article/details/90408393


#[break]
# break语句跳出了最内层的for循环，但还可以执行外层循环

# 作用：用来跳出最内层的for循环或者while循环，脱离该循环后程序从循环代码后面继续执行。
# 即break语句只能【跳出当前层次】的循环。

for j in [1, 2, 3]:
    if j == 2:
        break
    print(j, end=" ")
# 结果是：1
# 跳出当前层次


for i in "lianyj":

	for j in [1,2,3]:
		if i == "n":
			break
		print(i, end=" ")


# 程序执行结果为：l l l i i i a a a n y y y j j j

print("")

# [continue]
# 作用：结束当前当次循环，即跳出循环体中还没有执行的语句，但是并不跳出当前循环。

for i in "lianyj":
	if i == "n":
		continue
	print(i, end="")
#程序执行结果为：pyhon





# [pass]
# 作用：不做任何作用，只起到占位的作用。循环中使用 pass 不会跳出循环

for i in "python":
	if i == "t":
		pass
	print(i, end="")
#程序执行结果为：python

