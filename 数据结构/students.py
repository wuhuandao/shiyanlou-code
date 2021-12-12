#!/usr/bin/env python3
n = int(input("Enter the number of students:"))
data = {}  #用来存储数据的字典变量
subjects = ('Physice','Maths','History') #所有科目
for i in range(0,n):
    name = input('Enter the name of the student{}:'.format(i + 1)) #获取学生姓名
    marks = []
    for x in subjects:
        marks.append(int(input('Enter marks of {}:'.format(x)))) #获得每一科的分数
    data[name] = marks #创建键值对
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed:(")
    else:
        print(x,"passed:)")
#name 和 marks 是变量，name 用来存储学生的名称，marks 是个列表，用来存储输入的学生的成绩数据.
# data 是个字典，字典的键值对中，键指的是 name 的值，值指的是 marks 的值。
# 因此会使用 data[name] = marks 将学生数据存入到 data 字典。
#最后通过 for 循环遍历字典，x 为学生的 name，y 为学生成绩列表 marks，sum() 函数会将传入的列表进行加和。
