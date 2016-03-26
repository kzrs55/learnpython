#coding=utf-8
__author__ = 'zjutK'
import threading
from time import ctime,sleep

def func(name):
    for i in range(5):
        print('%s listening music at %s' %(name,ctime()))
        sleep(4)

def finc1(name):
    for i in range(5):
        print('%s watch movie at %s' %(name,ctime()))
        sleep(4)


if __name__ == '__main__':
    threads=[]
    threads.append(threading.Thread(target=finc1,args=('bob',)))
    threads.append(threading.Thread(target=func,args=('kent',)))
    print(threads)
    for i in threads:
        i.setDaemon(True) #守护线程,主线程结束守护线程也就结束了
        i.start()
    i.join()#在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

