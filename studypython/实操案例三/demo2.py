# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/3/7 12:51"

# @Filename :demo2.py

# 判断语句和循环语句
# 剪刀 0 石头 1 布 2

import random

x = int(input())

r = random.randint(0, 2)
if x == 0:
    print("你的输入为:剪刀（0）")
    print("系统随机生成数:", r)
    if r==2:
        print("你赢了")
    elif r==1:
        print("你输了")
    else:
        print("平局")
elif x == 1:
    print("你的输入为:石头（1）")
    print("系统随机生成数:", r)
    if r == 0:
        print("你赢了")
    elif r == 2:
        print("你输了")
    else:
        print("平局")
elif x == 2:
    print("你的输入为:布（2）")
    print("系统随机生成数:", r)
    if r == 1:
        print("你赢了")
    elif r == 0:
        print("你输了")
    else:
        print("平局")
else:
    print("玩游戏呢别闹")

if __name__ == '__main__':
    TheApp = 0
