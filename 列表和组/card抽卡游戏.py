import random
#调用random随机模块，进行抽卡

card_turple = ('武则天','项羽','嬴政','诸葛亮','高渐离','李白','程咬金','鲁班七号') 
#创建卡池,使用元组turple使卡池不可更改
package1 = [ ] #创建用户卡包,用来存放抽到的卡牌,需要能增加,删除数据,并排序,所以用列表.

while 1:
    #用户输入指令,
    # input '''可输出多行文字
    choose = int(input('''
    充值能让你变得更强!
     请选择指令:
     1.抽卡
     2.查看背包
     3.整理背包
     4.离开
     '''))
    
    #选1抽卡时,询问抽卡次数
    if choose == 1:
        num = int(input('请输入抽卡次数：'))
        for i in range(0,num):
            newcard = random.choice(card_turple)
            print("你抽到了：{}".format(newcard))
            package1.append(newcard)
        print("卡已存入卡包")        
    #抽卡random.choice
    #append命令放入背包package

    if choose == 2:  #输入2，查看背包内容
        for i in package1:
            print(i)

    if choose == 3:  #整理背包，并显示内容
        print('整理背包')
        package1.sort()
        for i in package1:
            print(i)
    #输入4，中断，退出。
    if choose == 4:
        break
