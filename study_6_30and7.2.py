import random
# print(random.random())
# print(random.randint(1,3))  #[1,3] 随机产生一个1<= and <=3的整数
# print(random.randrange(1,3)) #[1,3) 随机产生一个 1<= and <3的整数
# print(random.choice([1,'aaa',[1,5,6]])) #随机从choice([])中挑选一个值,注意()多个值需要放在列表中
# print(random.sample([1,'22',[1,2,3]],2)) #随机列表挑选N个元素进行组合
# print(random.uniform(1,3)) #随机产生一个 1< and <3的小数
# item=[1,2,3,4,5,6,7,8,9]
# random.shuffle(item)#打乱一个列表里面值的顺序
# print(item)

# # 验证码随机
# def make_code(size=4):
#     res = ''
#     for i in range(size):
#         s1 = chr(random.randint(65, 90))
#         s2 = str(random.randint(0, 9))
#         res += random.choice([s1, s2])
#     return res

# print(make_code())

import os
# os.getcwd()  #获取当前工作目录，即当前python脚本工作的目录路径
# # os.chdir('dirname') #改变当前脚本工作目录
# os.curdir #获取当前目录:('.') 返回值
# os.pardir #获取当前目录的父目录字符串名:('..') 返回值
# os.makedirs('dirname/dirname2') #可生成多层递归目录
# os.removedirs('dirname') #若目录为空，则删除，并递归到上一级目录，若也为空，则删除，依次类推
# os.mkdir('dirname') #生成单级目录；
# os.rmdir('dirname') #删除单级空目录，若目录不为空则无法删除。报错
# os.listdir('dirname') #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove() #删除一个文件
# os.stat('path/filename') #获取文件/目录信息
# os.sep #输出操作系统的路径分割符 win下为\\  Linux下为 /
# os.linesep #输出平台使用的行终止符 win为\r\n , Linux为\n
# os.name  #输出字符串指示当前使用平台
# os.pathsep    #输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.system("bash command")
# os.environ #获取环境变量,返回值是字典，key与value 都是字符串
# os.environ['aaaaaaaaaa']='11111111'  比如登录系统，用户登录成功之后的一系列操作，都需要以用户为基础

# os.path.abspath(__file__) #返回path规范化的绝对路径
# os.path.split(r'a\b\c\d.txt') #将path分割成目录和文件名二元组返回
# os.path.isabs() #如果path是绝对路径，返回True
# os.path.isfile() #如果path是一个存在的文件，返回True
# os.path.isdir() #如果path是一个存在的目录，返回True
# os.path.join() #path1[, path2[, ...]] #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime()  #返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime()  #返回path所指向的文件或者目录的最后修改时间
# os.path.getsize() #返回path的大小


# import sys
# sys.argv #命令行参数List

# import sys
# import time

# def progress(percent,width=50):
#     if percent >= 1:
#         percent=1
#     show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
#     print('\r%s %d%%' %(show_str,int(100*percent)),end='')


# #=========应用==========
# data_size=333333
# recv_size=0
# while recv_size < data_size:
#     time.sleep(0.01) #模拟数据的传输延迟
#     recv_size+=1024 #每次收1024

#     percent=recv_size/data_size #接收的比例
#     progress(percent,width=70) #进度条的宽度70
import time


def progress(percent):
    if percent > 1:
        percent = 1
    res=int(50 * percent) * '#'       
    print('\r[%-50s] %d %%' % (res, int(percent*100)), end='')


recv_data = 0
total_data = 23333
while recv_data < total_data:
    time.sleep(0.1)
    recv_data += 1024
    percent = recv_data / total_data
    progress(percent)
