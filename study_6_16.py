# 习题1
# x = 1
# def func():
#     print(x)
# def foo():
#     x = 222
#     func()
# x = 333
# foo()

# 习题2（需要反复会看此题）
# input=111
# def f1():
#     def f2():
#         print(input)
#     input=222
#     f2()
# f1()


# def func():
#     print('form func')
# # 1、可以被赋值
# # f=func
# # print(f,func)
# # f()

# # 2、可以当做函数参数传入
# def foo(x):
#     print(x)
#     x()

# foo(func)

# # 3、可以接收返回值
# # def foo(x):
# #     return x
# # res=foo(func)
# # print(res)
# # res()

# # 4、可以当做容器类型的一个元素
# # l=[func,222]
# # print(l)
# # l[0]()


# def login():
#     print('登录功能')


# def transfer():
#     print('转账功能')


# def check_banlance():
#     print('查询余额')


# func_dit = {'0':['退出系统',None],'1': ['登录',login], '2': ['转账',transfer], '3':['查询余额', check_banlance]}
# while 1:
#     for k in func_dit:
#         print(k,func_dit[k][0])
#     choice = input('请输入你的选择：').strip()


#     if not choice.isdigit():
#         continue
#     if choice == '0':
#         print('退出程序')
#         break
#     if choice in func_dit:
#         func_dit[choice][1]()
#     else:
#         print('输入的指令不存在')
    # if choice == '0':
    #     break
    # elif choice == '1':
    #     login()
    # elif choice == '2':
    #     transfer()
    # elif choice == '3':
    #     check_banlance()
    # else:
    #     print('输入的指令不正确')
    #     continue

# def f1():
# 	x=33333
# 	def f2():
# 		print(x)
# 	return f2  #返回的是f2的内存地址
# f=f1()
# f()