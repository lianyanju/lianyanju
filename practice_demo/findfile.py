import os
dir_list = os.listdir("../1")
# print(dir_list)
# ['.DS_Store', 'report.txt', '3', '2']

files = []
dir_lists=[]

for thisFile in dir_list:
#
    pathname = os.path.join("../1", thisFile)
    # print(pathname)
#
    if os.path.isfile(pathname):
        print(thisFile + "  isfile:")
        files.append(thisFile)
    else:
        print(thisFile + " is folder:")
        dir_lists.append(thisFile)
#
#
print("files: " ,files)
print("dir_lists: " ,dir_lists)