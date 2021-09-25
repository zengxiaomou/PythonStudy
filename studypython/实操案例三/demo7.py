# _*_ conding utf-8 _*_
__author__ = "zeng"
__data__ = "2021/3/28 20:23"
# @Filename : demo7.py


import schedule
import time

def job():
    print("Haha")

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    TheApp = 0