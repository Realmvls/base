#!/usr/bin/Python
# -*- coding: utf-8 -*-
# import time
# def sleeptime(hour,min,sec):
#     return hour*3600+min*60+sec;
# sleep_time = sleeptime(0,0,2);
# n = 1
# while n<3:
#     n = n+1
#     time.sleep(sleep_time);
#     print("每隔2秒显示一次")
# else:
#     exit()


#随机数种子
import random
import datetime

random.seed(datetime.datetime.now())
print (random.random())