"""
闭包函数： 霍格沃兹开学啦，要求打印每个学生的姓名、性别、年级
"""


# # 函数引用
# def hogwarts():
#     print("霍格沃兹测试学社")
# # hogwarts() # 函数的调用
# # print(hogwarts)
# # print("==========")
# # harry = hogwarts # 把函数对象赋值给一个变量
# # print(harry)
# peter = hogwarts
# print(peter)
# peter()

# def output_students(name, gender, grade):
#     print(f"霍格沃兹开学啦， 学生名称是{name}，性别是{gender}， 年级是{grade}年级")
#
# output_students("哈利", "男生", 2)
# output_students("罗恩", "男生", 2)
# output_students("赫敏", "女生", 2)

# 演变：发现grade是功能的这些小朋友都是2年纪，
# 把变的逻辑封装成内部函数

def students_grade(grade):
    def output_students(name, gender):
        print(f"霍格沃兹开学啦， 学生名称是{name}，性别是{gender}， 年级是{grade}年级")
    return output_students
    #return 的是内部函数的对象：output_students


students_info = students_grade(1)
students_info("罗恩", "男生")
students_info("哈利", "男生")
students_info("赫敏", "女生")
