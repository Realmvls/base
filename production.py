#!/usr/bin/Python
# -*- coding: utf-8 -*-
#多线程生产者消费者问题

from random import randint
from time import sleep
import queue
import os
import productionThread


os.chdir('F:\\github\\base')
def writeQ(queue):
    print('producing object for Q...',queue.put('xxx',1))
    print('size now',queue.qsize())

def readQ(queue):
    va1 = queue.get(1)
    print('consumed object from Q...size now',queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = queue(32)

    threads = []
    for i in nfuncs:
        t = productionThread.thisThread(funcs[i],(q,nloops),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')

if __name__ == '__main__':
    main()
