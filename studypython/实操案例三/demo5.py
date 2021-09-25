# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/3/10 22:09"


# @Filename : demo5.py


def hengxian():
    return "---"


hengxian()


def duoHx(n):
    he = hengxian() * n
    print(he)


duoHx(5)


def addNum(a, b, c):
    return a + b + c

def avgNum(a,b,c):
    return addNum(a, b, c)/3

print(avgNum(1,2,3))

if __name__ == '__main__':
    TheApp = 0
