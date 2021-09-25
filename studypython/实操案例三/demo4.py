# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/3/7 21:58"
# @Filename : demo4.py

# 新建商品列表
product_list = [
    ("iphone", 6888),
    ("macpro", 9800),
    ("bicycle", 200),
    ("coffee", 31),
    ("book", 21)
]

# 商品列表
print("--------商品列表-------")
for i in range(len(product_list)):
    print(i, end="\t")
    print(product_list[i][0], end="\t")
    print(product_list[i][1])

# 购物车
gouwuche = []
while True:
    x = input("请输入商品编号:")
    if (x!='q' and int(x) >= 0 and int(x) < len(product_list)):
        x = int(x)
        gouwuche.append(product_list[x])
    elif (x == 'q'):
        for i in range(len(gouwuche)):
            print(i, end="\t")
            print(gouwuche[i][0], end="\t")
            print(gouwuche[i][1])
        break;  # 退出循环
    else:
        print("编号不正确，请重新输入")




if __name__ == '__main__':
    TheApp = 0
