"用Pyhon设计第一个游戏"
import random
sec=random.randint (1,10)

temp=input("\t不妨猜一下老实本分豪心里想的是哪个数字:")
guess=int(temp)

if guess==8:
    print("\t你是我的小号么！？，你怎么知道我想的是这个！！")
    print("\t哼，猜中了也没奖励~")
else:
    while guess!=sec:
        temp=input("\t哎呀，猜错了，请重新输入吧:")
        guess=int(temp)
        if guess==sec:
            print("\t你是我的小号么！？，你怎么知道我想的是这个！！")
            print("\t哼，猜中了也没奖励~")
        else:
            if guess>sec:
                print("\t哥，咱整大了")
            else:
                print("\t哥，这次小了小了")
        """    print("好弱哦，我心里藏的是8")"""
print("游戏结束，不玩啦，23333333")
