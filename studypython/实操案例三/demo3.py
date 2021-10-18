# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/3/7 16:22"
# @Filename : demo3.py

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d " % (i, j, i * j),end="\t")
    print()

if __name__ == '__main__':
    TheApp = 0
