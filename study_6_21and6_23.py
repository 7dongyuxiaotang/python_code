# def deco1(func1):
#     def warpper1(*args, **kwagrs): #func1 = wrapper2的内存地址
#         print('正在运行===》deco1.warpper1')
#         res1 = func1(*args, **kwagrs)
#         return res1
#     return warpper1


# def deco2(func2):
#     def warpper2(*args, **kwagrs):  #func2 = wrapper3的内存地址
#         print('正在运行===》deco2.warpper2')
#         res2 = func2(*args, **kwagrs)
#         return res2
#     return warpper2


# def deco3(x):
#     def outer3(func3):
#         def warpper3(*args, **kwagrs): #fun3=被装饰对象index函数的内存地址
#             print('正在运行===》deco3.outer3.warpper3')
#             res3 = func3(*args, **kwagrs)
#             return res3
#         return warpper3
#     return outer3


# #加载顺序自下而上
# @deco1      #index=deco1(warpper2的内存地址)===》index = wrapper1的内存地址
# @deco2      #index=deco2(warpper3的内存地址)===> index = wrapper2的内存地址
# @deco3(111) #===》@outer3 ====> index=outer(index)====>index=warpper3的内存地址
# def index(x, y):
#     print('from index %s %s ' % (x, y))

# #执行顺序是自上而下的
# index(1, 2)


# def func(name):
#     print('%s程序开始运行'%name)
#     while True:
#         x = yield None
#         print('%s程序运行中，x的值等于%s'%(name,x))

# def func(name):
#     print('%s程序开始运行' % name)
#     x = yield 1111  # x=jjj
#     print('%s程序运行中，x的值等于%s' % (name, x))
#     print('哈哈哈')
#     print('hahaha')
#     yield 222


# f = func('不好理解的')
# res = f.send(None)  # next(f)
# print(res)
# res2 = f.send('jjj')
# print(res2)

# x=2
# y=3

# print(x if x > y else y)


# 列表生成式
#[expression for item1 in iterable1 if condtion1]

# l=['你好啊','你啊','我啊','我去','啊啊啊','呵呵']
# new_l=[name for name in l if name.endswith('啊')]
# print(new_l)

# l=['alex_dsb','lxx_dsb','wxx_dsb','xxq_dsb','eogn']
# new_l=[name.strip('_dsb').upper() for name in l if name.endswith('_dsb')]
# print(new_l)

# keys = ['name', 'age', 'gender']
# dic = {key: None for key in keys}
# print(dic)

# items = [('name', 'egon'), ('age', '18'), ('gender', 'male')]
# res = {k: v for k, v in items if k != 'gender'}
# print(res)

# keys=['name','age','gender']
# set1={key for key in keys}
# print(set1,type(set1))

# with open(r'D:\222.txt',mode='rt',encoding='utf-8') as f:
#     方式一：
    # res = 0
#     for line in f:
#         res += len(line)
#     print(res)
#     方式二：
    # res=sum([len(line) for line in f])
    # ret=[len(line) for line in f]
    # print(ret)
    # print(res)
#     方式三：
#     res=sum(len(line) for line in f)
#     print(res)

#直接调用
# def f1():
#     print('循环往复')
#     f2()



#间接调用
# def f1():
#     print('循环往复')
#     f2()


# def f2():
#     print('梅开二度')
#     f1()


# f1()


# def f1(n):
#     if n > 10:
#         return 
#     print(n)
#     n +=1
#     f1(n)

# f1(0)

# def age(n):
#     if n ==1:
#         return 18
#     return age(n-1)+10

# print(age(5))


def f1(l):
    for x in l:
        if type(x) is list:
            f1(x)
        else:
            print(x)

l=[1,2,[3,[4,[5,[6,[7,8,9,10,[11,12,[13,14]]]]]]]]
f1(l)

