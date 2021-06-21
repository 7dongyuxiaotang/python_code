# l = ['张三', '李四', '王五']
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# s1 = ''
# s1.__iter__()
# l = []
# l.__iter__()
# t = (1,)
# t.__iter__()
# d = {'a': 1,'b':2,'c':3}
# ret=d.__iter__()
# while 1:
#     try:
#         print(ret.__next__())
#     except StopIteration:
#         break

# set1 = {1, 2, 3}
# set1.__iter__()
# with open(r'D:\a.txt',mode='rt',encoding='utf-8') as f:
#     l=[]
#     for line in f:
#         l.append(line.strip().split(':'))
#         res=dict(l)
#     f1=res.__iter__()
#     while True:
#         try:
#             print(f1.__next__())
#         except StopIteration:
#          break

# d = {'a': 1,'b':2,'c':3}
# for k in d:
#     print(k)

# def func():
#     print('第一次')
#     yield 1
#     print('第二次')
#     yield 2
#     print('第三次')
#     yield 3
#     print('第四次')

# g=func()
# g.__iter__()
# g.__next__()
# print(g.__next__())


def my_range(start, stop, stpe=1):
    print('start')
    while start < stop:
        yield start
        start += stpe
    print('end')



for n in my_range(1,7,2):
    print(n)
