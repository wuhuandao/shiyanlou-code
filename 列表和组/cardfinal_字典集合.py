import random
import time

## 创建卡池
card_tuple = ('武则天','嬴政','诸葛亮','宫本武藏','李白')
## 定义卡的权重
weight_list = (5, 10, 50, 50, 100)
## 定义用于比较的权重列表
weight_compare = (5, 15, 65, 115, 215)
## 创建背包
package_dic = {}
###临时卡包
card_list = [ ]
## 主程序
while 1:
    ## 接收用户的选择指令
    choose = int(input('''
    充值能让你变得更强！
    请选择指令：
    1. 抽卡
    2. 查看背包
    3. 离开
    '''))

    ## 当用户输入 1 时，先询问抽卡次数
    if choose == 1:
        num = int(input('输入抽卡次数：'))
        #根据权重列表判断卡片;
        #<=5为武则天,<=15为嬴政,<=65诸葛亮,<=115宫本武藏,<=215李白
        for i in range(0,num):
            rand_num = random.randint(1,214)
            i += 1
            if rand_num <= 5:
                newcard = card_tuple(0)
                print("你抽到的卡是：{}".format(newcard))
                card_list.append(newcard)
                time.sleep(0.3)
            elif rand_num <=15:
                newcard = card_tuple(1)
                print("你抽到的卡是：{}".format(newcard))
                card_list.append(newcard)
                time.sleep(0.3)
            elif rand_num <= 65:
                newcard = card_tuple(2)
                print("你抽到的卡是:{}".format(newcard))
                card_list.append(newcard)
                time.sleep(0.3)
            elif rand_num <=115:
                newcard = card_tuple(3)
                print("你抽到的卡是:{}".format(newcard))
                card_list.append(newcard)
                time.sleep(0.3)
            else:
                newcard = card_tuple(4)
                print("你抽到的卡是:{}".format(newcard))
                card_list.append(newcard)
                time.sleep(0.3)
            time.sleep(0.3) 
        ## 完成抽完后，提示卡已存入背包    
        print('卡已存入背包')
        print('________________')
    wzt = card_list.count('武则天')
    package_dic['武则天'] = '数量：wzt'
    yz = card_list.count('嬴政')
    package_dic['嬴政'] = "数量：{}".format(yz)
    zgl = card_list.count('诸葛亮')
    package_dic['诸葛亮'] = '数量：zgl'
    gbwz = card_list.count('宫本武藏')
    package_dic['宫本武藏'] = '数量：gbwz'
    lb = card_list.count('李白')
    package_dic['李白'] = '数量：李白'
    ## 当用户输入 2，打印背包内容
    if choose == 2:
        ## 分背包有卡片和背包没卡片两种情况
        if len(package_dic) == 0:
            print('背包暂无英雄，快去抽卡吧')
            print('________________')
        else:
            for key in package_dic():
                print(key)

    ## 当用户输入 3，退出程序
    if choose == 3:
        break

