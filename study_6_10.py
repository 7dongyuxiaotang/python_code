# feek的应用
# import time
# with open(r'D:\access.log',mode='rb') as f:
#     f.seek(0,2)
#     while True:
#         line=f.readline()
#         if len(line) == 0:
#             time.sleep(0.3)
#         else:
#             print(line.decode('utf-8'),end=' ')

# 普通方式修改文件
# with open(r'D:\text.txt',mode='r+t',encoding='utf-8') as f:
#     f.seek(3,0)
#     f.write("不")

# 第一种方式
# with open(r'D:\text.txt',mode='rt',encoding='utf-8') as f:
#     res=f.read()
#     data=res.replace('alex','sb')
# with open(r'D:\text.txt',mode='wt',encoding='utf-8') as f1:
#     f1.write(data)

# 第二种方式
# with open(r'D:\text.txt',mode='rt',encoding='utf-8') as f,\
#     open(r'D:\.c.txt.swap',mode='wt',encoding='utf-8')  as f1:
#     for line in f:
#         f1.write(line.replace('alex','dsb'))

# def 函数名(参数1、参数2、...):
#     """
#     文档描述
#     """
#     函数体
#     return 值


# 定义函数发生的事情
# 1、申请内存空间保存函数体代码
# 2、将上述内存地址绑定函数名
# 3、定义函数不会执行函数体代码，但是会检测函数体语法

# 调用函数发生的事情
# 1、通过函数名找到函数的内存地址
# 2然后加( )号就是在触发函数体代码的执行

# 形式一：无参函数
# def func():
#     print('haha')
# func()

# 形式二、有参函数
# def func(x,y):
#     print(x,y)

# func(4,5)

# #形式三、空函数
# def func(x,y):
#     pass

# def auth_user():
#     '''user authentication funtion'''
#     pass
# def download_file():
#     '''download file function'''
#     pass
# ...


# def add(x,y):
#     return x,y,x+y

# ret=add(1,2)
# print(ret,type(ret))

# 形参 实参
# def func(x,y):
# 	print(x,y)
# # func(y=10,x=20)

# func(1,2,x=3)

# def func(y=3,x):
#     pass

# m=[111111]
# def func(x,y=m):
#     print(x,y)
# m.append(3333333)
# func(1)

# def func(x,y,z,l=None):
#     if l is None:
#         l=[]
#     l.append(x)
#     l.append(y)
#     l.append(z)
#     print(l)
# func(1,2,3)
# func(12,2,3,[111,222])


#可变长度的位置参数
# def add(*args):
#     ret = 0
#     for item in x:
#         ret += item
#     return ret


# res = add(1, 5, 6, 3, 2, 7, )
# print(res)


#可变长度的关键字形参
# def func(x,y,**kwargs):
#     print(x,y,kwargs)

# func(6,y=1,z=2,c=5)

# def func(x,y,*args): #args=(1,2,3,4,5)
# 	print(x,y,args)
# func(1,2,*[1,2,3,4,5]) #func(1,2,1,2,3,4,5)


# def func(x,y,z): 
# 	print(x,y,z)
# func(*{'x':1,'y':2,'z':3}) #如果加一个*就是 拆分成了func('x','y','z')
# '''
# x y z
# '''
# func(**{'x':1,'y':2,'z':3})#如果加** 就是，拆分成了func(x=1,y=2,z=3)


#*args必须在 **kwargs之前
# def func(x,**kwargs,*args):
# 	pass

# def func(x,y,**kwarges): 
# 	print(x,y,kwarges)

# func(**{'x':1,'y':2,'z':3,'c':5,'b':6})