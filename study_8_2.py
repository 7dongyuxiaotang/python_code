# while (1):
#     age = input('>>>').strip()  # 只要输入的不是数字，就会出错
#     if age.isdigit():
#         age = int(age)
#         if age > 18:
#             print('猜大了')
#         elif age < 18:
#             print('猜小了')
#         else:
#             print('猜对了')
#             break
#     else:
#         print('必须输入数字')

# try:
#     # 子代码块 有可能会抛出异常的代码
#     print('子代码1')
#     print('子代码2')
#     print('子代码3')
#
# except 异常类型1 as e:
#     pass
# except 异常类型2:
#     pass
#
# ...
# else:
# # 如果被检测的子代码块没有异常发生，则会执行else的子代码
# pass
#
# finally:
# # 无论被检测的子代码有无异常发生，都会执行finally的子代码
# pass

# print('start')
#
# try:
#     print('第一个BUG')
#     l = ['aaa', 'bbb']
#     # l[3]
#     print('第二个BUG')
#     xxx
#     print('第三个BUG')
#     dic = {'a': 1}
#     dic['aaa']
#
# except IndexError as e:
#     print('异常信息：', e)
#
# except Exception as e:
#     print('所有异常都可以匹配')
# print('end')


