# bubble 冒泡
# def bubbleSort(arr):
#     n = len(arr)
#
#     print(range(n))
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 自己写的

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for i in range(n-1):
            demo = 0
            if arr[i] > arr[i + 1]:
                demo = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = demo





arr = [64, 34, 25, 12, 22,  90, 11]

print("排序前的数组:")
print(arr)

bubbleSort(arr)

print("排序后的数组:")
print(arr)
