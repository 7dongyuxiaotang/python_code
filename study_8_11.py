# from multiprocessing import Process, current_process
# import time
# import os
#
#
# def task():
#     print('%s is running' % current_process().pid)
#     print('子进程的父进程的pid号：%s' % os.getppid())
#     time.sleep(50)
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     print('主程序pid号:%s' % os.getpid())
#     print('主程序的父程序pid号：%s' % os.getppid())


# 守护进程
# import time
# from multiprocessing import Process
#
#
# def task(name):
#     print('%s活着' % name)
#     time.sleep(10)
#     print('%s死亡' % name)
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=('子进程',))
#     p.daemon =True
#     p.start()
#     time.sleep(3)
#     print('主进程死了')


# 互斥锁
from multiprocessing import Process, Lock
import time
import json
import random


def search(name):
    with open(r'D:\python\grammar\2021.8.11\ticket.txt', mode='r', encoding='utf-8') as f:
        dic = json.load(f)
    print('用户%s正在查票,票的剩余量为:%s' % (name, dic.get('ticket_num')))


def buy(name):
    with open(r'D:\python\grammar\2021.8.11\ticket.txt', mode='r', encoding='utf-8') as f:
        dic = json.load(f)
        time.sleep(random.randint(1, 3))
    if dic.get('ticket_num') > 0:
        print('用户%s购票成功' % name)
        dic['ticket_num'] -= 1
        with open(r'D:\python\grammar\2021.8.11\ticket.txt', mode='w', encoding='utf-8') as f:
            json.dump(dic, f)
    else:
        print('用户%s购票失败，票数余量不足' % name)


def run(name, mutex):
    search(name)
    # 给买票环节加锁
    mutex.acquire()
    buy(name)
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    # 在主进程中生成一把锁，让所有的子进程抢，谁抢到谁先买
    mutex = Lock()
    for i in range(1, 10):
        p = Process(target=run, args=(i, mutex))
        p.start()
