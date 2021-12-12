#!/usr/bin/env python3
n = int(input("Enter the value of n:"))
print("Enter values for the Matiex A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multipication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5),end=' ')
    print()
print("-" * 7 * n)
#这里我们使用了几次列表推导式. [int(x) for x in input().split()] 
# 首先通过 input() 获得用户输入的字符串，
# 再使用 split() 分割字符串得到一系列的数字字符串，
# 然后用 int() 从每个数字字符串创建对应的整数值。
# 我们也使用了 [a[i][j] * b[i][j] for j in range(n)] 来得到矩阵乘积的每一行数据。