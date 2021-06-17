# 解决方案一：
# import time


# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))


# statr = time.time()
# index(111, 222)
# stop = time.time()
# print(stop-statr)


# 解决方案二：
# import time


# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))

# def wapper():
# 	statr = time.time()
# 	index(111, 222)
# 	stop = time.time()
# 	print(stop-statr)

# wapper()


# 解决方案二的优化一：
# import time


# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))

# def wapper(*args,**kwargs):
# 	statr = time.time()
# 	index(*args,**kwargs)
# 	stop = time.time()
# 	print(stop-statr)

# wapper(111,222)


# 解决方案二的优化二：
# import time

# def home(name):
# 	time.sleep(2)
# 	print('welcome %s come home' %name)
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))

# def outter(func):
# 	#func=index的内存地址
# 	def wapper(*args,**kwargs):
# 		statr = time.time()
# 		func(*args,**kwargs) #调用index函数
# 		stop = time.time()
# 		print(stop-statr)
# 	return wapper
# index=outter(index)  #首先将index函数的内存地址给了outter，wapper就会调用index函数，最后将wapper的内存地址返回，用index变量接收wapper内存地址
# index(1,2) #此时的index调用的其实是wapper函数，而不是直接调用index函数
# home=outter(home)
# home('zhangs')  #此时可以将装饰器给多个函数

# 解决方案二的优化三：
# import time


# def home(name):
#     time.sleep(2)
#     print('welcome %s come home' % name)


# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     return 123


# def outter(func):
#     def wapper(*args, **kwargs):
#         statr = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop-statr)
#         return res
#     return wapper


# index = outter(index)
# ret = index(1, 2)
# print(ret)


# 语法糖
# import time


# def outter(func):
#     def wapper(*args, **kwargs):
#         statr = time.time()
#         res = func(*args, **kwargs)  # 用变量res接收函数index的返回值
#         stop = time.time()
#         print(stop-statr)
#         return res  # 返回index函数的返回值
#     return wapper


# @outter
# def home(name):
#     time.sleep(2)
#     print('welcome %s come home' % name)


# @outter
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     return 123  # 被修饰的函数拥有返回值


# index(1,2)
