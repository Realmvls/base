#!/usr/bin/Python
# -*- coding: utf-8 -*-
import time
def timedecorate(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('This func run time is {}'.format(stop_time-start_time))
        return res
    return deco
@timedecorate
def test1():
    time.sleep(1)
    print('first test')
    return

@timedecorate
def test2():
    time.sleep(2)
    print('second test')

test1()
test2()
