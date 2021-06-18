# 无参装饰器模板
# def outer(func):
#     def wapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wapper


# @outer
# def time():
#     pass

# time()

# 装饰器补充
# import time
# from functools import wraps

# def outter(func):
#     # @wraps(func)
#     def wapper(*args, **kwargs):
#         statr = time.time()
#         res = func(*args, **kwargs)  # 用变量res接收函数index的返回值
#         stop = time.time()
#         print(stop-statr)
#         return res  # 返回index函数的返回值
#     return wapper


# # @outter
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     return 123  # 被修饰的函数拥有返回值


# index(1, 2)
# print(index.__name__)


# 有参装饰器
# def outer(db_type):
#     def auth(func):
#         def wapper(*args, **kwargs):
#             name = input('请输入你的用户名：').strip()
#             pwd = input('请输入你的密码：').strip()
#             if db_type =='file':
#                 print('基于文件的数据')
#                 res= func(*args, **kwargs)
#                 return res
#             elif db_type == 'mysql':
#                 print('基于数据库的数据')
#                 res= func(*args, **kwargs)
#                 return res
#             elif db_type =='ldap':
#                 print('基于ldap的数据')
#                 res= func(*args, **kwargs)
#                 return res
#         return wapper
#     return auth

# @outer('file')
# def file(x,y):
#     print('file——>%s,%s'%(x,y))

# @outer('mysql')
# def mysql(x,y):
#     print('mysql——>%s,%s'%(x,y))

# @outer('ldap')
# def ldap(x,y):
#     print('ldap——>%s,%s'%(x,y))

# mysql(1,2)