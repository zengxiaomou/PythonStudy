# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/4/6 7:49"
# @Filename : demo1.py

year=[82,89,88,86,85,00,99 ]
print(year)
for index,value in enumerate(year):
   # print(index,value)
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
print(year)

if __name__ == '__main__':
    TheApp = 0