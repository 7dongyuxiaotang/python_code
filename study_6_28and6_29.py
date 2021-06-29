# import foo
# import sys
# print(sys.path)

# print(sys.modules)
# 绝对导入---- -> sys.path--- -> 执行文件
# sys.path.append('r/Users/..../项目的根目录')
# print(__file__)

# import datetime
# import time
# print(time.time())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d %X'))
# print(time.localtime())
# print(time.localtime().tm_year)
# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(days=3))
# print(datetime.datetime.now()+datetime.timedelta(weeks=3))


#需要掌握的操作
# import time

# s_time=time.localtime()
# print(time.mktime(s_time))

# tp_time=time.time()
# print(time.localtime(tp_time))
import time
# s_time=time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))
# res=time.strftime('%Y-%m-%d %H:%M:%S')
# print(time.strptime(res,'%Y-%m-%d %H:%M:%S'))

#format string——> 结构化时间 ——>timestamp
# struct_time=time.strptime('2021-6-29 20:32:00','%Y-%m-%d %H:%M:%S') #将字符格式的时间转化为结构化时间
# time_stamp=time.mktime(struct_time)+7*86400

# res=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time_stamp))
# print(res)

# import datetime
# # print(time.asctime())
# print(datetime.datetime.fromtimestamp(1))