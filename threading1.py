# !/usr/bin/Python
# -*- coding: utf-8 -*-
# import time, threading
# # threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread
# def loop():
#     print('thread %s 开始' % threading.currentThread().getName())
#     n = 0
#     while n < 5:                                                                  #t1 = threading.Thread(target=run_thread, args=(5,),name='LoopThread')
#         n = n + 1
#         print('thread %s >>> %s' % (threading.currentThread().getName(), n))
#         time.sleep(1)
#     print('thread %s 结束.' % threading.currentThread().getName())
# #方法1
# for x in range(3):
#     t = threading.Thread(target = loop)
#     t.start()
# t.join()
# print('thread %s ended.' % threading.currentThread().getName())
#开始线程也可以用下面这种方法写   方法2
# t = threading.Thread(target=loop,name='LoopThread1')
# t2 = threading.Thread(target=loop,name='LoopThread2')
# t.start()
# t2.start()
# t.join()
# t2.join()    #jocin()方法让线程逐条执行
# print('thread %s ended.' % threading.currentThread().getName())


############################################################################################################################################
#
# import time
# import threading
#
# class loop(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         print('thread %s 开始' % threading.currentThread().getName())
#         n = 0
#         while n < 5:
#             n = n + 1
#             print('thread %s >>> %s' % (threading.currentThread().getName(), n))
#             time.sleep(1)
#         print('thread %s 结束.' % threading.currentThread().getName())
# if __name__ == '__main__':
#     threads = []
#     for j in range(3):
#         t = loop()
#         threads.append(t)
#     for thr in threads:
#         thr.start()
#     for thr in threads:
#         """
#         isAlive()方法可以返回True或False，用来判断是否还有没有运行结束
#         的线程。如果有的话就让主线程等待线程结束之后最后再结束。
#         """
#         if thr.isAlive():
#             thr.join()
#     print('thread %s ended.' % threading.currentThread().getName())
############################################################################################################################################


#线程锁相关的问题
#join()方法是对整个线程做限制。而线程锁lock.acquire是在线程执行过程中对某一部分进行锁限制
#
# import threading
# import time
# lock=threading.RLock()
# gunm = 0
# def work(max_number):
#     for i in range(max_number):
#         print(i)
# def myblock():
#     work(3)
#     time.sleep(1.5)
#     lock.acquire()
#     global gunm
#     gunm = gunm + 1
#     print('gunm is {}'.format(gunm))
#     lock.release()
# for x in range(4):
#     t = threading.Thread(target = myblock)
#     t.start()
# t.join()
# print('主线程结束')

# GIL是python的全局解释器锁的简称。这个锁是干什么用的呢？说白了就是限制python解释调用cpu内核之用的.
# 多线程理论上可以同时调用多个cpu内核同时工作，比如java语言就可以做到。但是python因为GIL的存在，
# 同一时间只有一条进程在cpu内核中进行处理。虽然我们可以看到多线程并发运行，但是那只是因为cpu内核通过
# 上下文的切换快速将多个线程来回执行造成的假象。python和java那种可以真正调用多核心多线程的语言，
# 在效率上还是有差异的。这个就是python一直被人诟病的GIL锁。


###################################################################################################################################

#队列queue 多应用在多线程应用中，多线程访问共享变量。对于多线程而言，访问共享变量时，队列queue是线程安全的
# import queue
#
# q=queue.Queue(5)    #如果不设置长度,默认为无限长
# print(q.maxsize)    #注意没有括号
# q.put(123)
# q.put(456)
# q.put(789)
# q.put(100)
# q.put(111)
#
# print(q.get())
# print(q.get())

#消费者生产者问题  （并不建议用这种写法，这种写法会在内存中创建一个无线大的队列，时间过一会会卡）

import queue,time,threading

q = queue.Queue()
def product(num):
    while True:
        try:
            q.put(int(num),'商品')

        except Exception as e:
            print(e)
def consumer(num):
    while True:
        print(num,q.get())
        time.sleep(0.1)
for i in range(5):
    t = threading.Thread(target=product,args=(i,))
    t.start()
for j in range(300):
    t = threading.Thread(target=consumer,args=(j,))
    t.start()
