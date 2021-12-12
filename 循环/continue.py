#要求用户输入一个整数，如果是负数，再次要求输入，
# 如果是整数，则计算该数的平方。
# 输入0，可以终止循环。
#！/usr/bin/env python3
while True:  #当条件为真时，持续loop，及无限循环，需要break来终止。
    n = int(input("请输入一个整数："))
    if n < 0:
        print("请重新输入")
        continue  #跳回循环的开始重新执行
    elif n == 0:
        break     #输入0 中断循环
    print("Square is/平方等于",n ** 2)
print("Goodbye,再见")