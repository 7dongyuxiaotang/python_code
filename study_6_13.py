# 名称空间优先级

# input = 333
# def func():
#     # input = 222
#     print(input)
# func()

# input = 333
# def func():
#     input = 222

# func()
# print(input)

# x = 1
# def func():
#     print(x)
# def foo():
#     x = 222
#     func()
# foo()

# def foo():
#     x=111
#     print(x)
#     print(y)
# def func():
#     y=222
#     print(x)
#     print(y)
# x=333
# y=444
# foo()
# func()

# global
# x=111
# def func():
#     x=222
# func()
# print(x)

# nonlocal
# x = 111


# def f1():
#     x = 222

#     def f2():
#         nonlocal x
#         x = 333
#     f2()
#     print(x)

# f1()


# x=111
# def func():
# 	print(x)	
# func()