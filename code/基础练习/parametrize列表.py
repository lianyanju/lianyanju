# 切片
# 列表的切片，列表的下标从0开始且采用前闭后开原则，所以下标取值范围是1~3，步长为2，所以是对应的值为[2,4]
s = [1,2,3,4,5,6]
print(s[1:4:2])


#extend、append、add

# 以下哪个选项是对应的正确操作
#  选项A： list_a.extend([4,5])    extend 操作过后变为[1,2,3,4,5]，
#  选项B： list_a.append([4,5])    append 之后为[1, 2, 3, [4, 5]]
#  选项C： list_a.add([4,5])       list没有add方法


# extend是将()中的列表元素追加到原列表之后，所以选extend。【两个列表合并】


def aa(name):
    b =3
    print("sdd")
    return name

aa("ll")