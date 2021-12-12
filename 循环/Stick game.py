#!/usr/bin/env python3
# 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1 到 4 根棍子。谁选到最后一根棍子谁就输。
# 判断一下用户有赢的机会吗？如果没有的话，如何修改游戏规则可以使用户有赢的机会呢？
# 特别说明：用户和电脑一次选的棍子总数只能是 5。
sticks = 21
print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("一共有21根木棍，每次请任选1-4根。")
print("Whoever will take the last stick will lose")
print("选择最后一根木棍的人判负")
while True:
    print("Sticks left/木棍剩余数量：", sticks)
    if sticks == 1:
        print("you took the last stick,you lose")
        print("你选到了最后一根，你输了￣へ￣")
        break
    sticks_taken = int(input("Take sticks(1-4)/选择木棍数量："))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("wrong choice/选择错误，请重新输入")
        continue
    print("Computer took/AI选择数量：", (5-sticks_taken),"\n")
    sticks -= 5
