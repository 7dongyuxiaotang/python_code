from multiprocessing import Queue, Process, JoinableQueue
import time
import random
from threading import Thread

# def producer(q):
#     q.put('队列里面的信息')
#     print('hello world')
#
#
# def consumer(q):
#     print(q.get())
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=producer, args=(q,))
#     p1 = Process(target=consumer, args=(q,))
#     p.start()-
#     p1.start()


# def producer(name, food, q):
#     for i in range(5):
#         data = '%s生产了%s%s' % (name, food, i)
#         # 模拟延迟
#         time.sleep(random.randint(1, 3))
#         print(data)
#         # 将数据丢入队列
#         q.put(data)
#
#
# def consumer(name, q):
#     while True:
#         food = q.get()
#         time.sleep(random.randint(1, 3))
#         print('%s吃了%s' % (name, food))
#         q.task_done()  # 告诉队列已经从里面取出了一个数据并且处理完毕
#
#
# if __name__ == '__main__':
#     # q = Queue()
#     q = JoinableQueue()
#     p1 = Process(target=producer, args=('大厨', '包子', q))
#     p2 = Process(target=producer, args=('tank', '饺子', q))
#     c1 = Process(target=consumer, args=('张三', q))
#     c2 = Process(target=consumer, args=('小三', q))
#     p1.start()
#     p2.start()
#     c1.daemon = True
#     c2.daemon = True
#     c1.start()
#     c2.start()
#     p1.join()
#     p2.join()
#     q.join()  # 等待队列中所有的数据被取完再往下执行代码

'''
JoinableQueue 每当该队列中存入数据的时候，内部会有一个计数器+1
每当调用task_done的时候，计数器-1
q.join()当计数器为0的时候，才往后运行
'''


# 只要q.join执行完毕，说明消费者已经处理完数据了，消费者就没有存在的必要了


# def task(name):
#     print('%s is running' % name)
#     time.sleep(1)
#     print('%s is over' % name)


# 开启线程不需要在main下面执行代码，直接书写就可以
# 但是还是习惯性的将启动命令写在main下面


class MyThead(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running' %self.name)
        time.sleep(1)
        print('%s is over' % self.name)

if __name__ == '__main__':
    # t = Thread(target=task, args=('egon',))
    # t.start()  # 创建线程的开销非常小  几乎是代码一执行，线程就可以创建了
    # print('主')
    t = MyThead('egon')
    t.start()
    print('主')