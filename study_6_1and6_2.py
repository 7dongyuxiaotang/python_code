# import copy
# list1=[1,2,[3,4]]
# list3=copy.deepcopy(list1)
# print(list3)
# print(id(list1[0]),id(list1[1]),id(list1[2]))
# print(id(list3[0]),id(list3[1]),id(list3[2]))
# list1[2][0]=5
# print(list3[2][0])
# print(list1[2][0])

# while循环
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# 循环的应用
# 1、结束循环
# 方法一、条件改为False
# i = 1
# while (i==1):
#     name = input("请输入你的帐号：")
#     password = input("请输入你的密码：")
#     if (name == "张三" and password == "123456"):
#         print("登录成功")
#         i = 0
#     else:
#         print("帐号或者密码错误")
# print("===end===")

# 方法二、break：跳出本次循环
# while (True):
#     name = input("请输入你的帐号：")
#     password = input("请输入你的密码：")
#     if (name == "张三" and password == "123456"):
#         print("登录成功")
#         break
#     else:
#         print("帐号或者密码错误")
# print("===end===")

# while嵌套与结束
# i = 1
# s = 1
# while (i <= 3 and s == 1):
#     name = input("请输入你的帐号：")
#     password = input("请输入你的密码：")
#     if (name == "张三" and password == "123456"):
#         print("登录成功")
#         while(s == 1):
#             print("主菜单：1、查询余额 2、转账 3、取款 0、退出系统")
#             cmd = input("请输入要进行的操作：")
#             while(cmd != "0"):
#                 if (cmd == "1"):
#                     print("您的账户余额是0")
#                     input("按下0：返回主菜单")
#                     break
#                 elif (cmd == "2"):
#                     transfer_account = input("请输入要转账的账户：")
#                     trasfer_money = input("请输入要转账的金额：")
#                     print("转账失败，账户内金额不足")
#                     input("0：返回主菜单：")
#                     break
#                 elif (cmd == "3"):
#                     draw = input("请输入要取款的金额：")
#                     print("取款失败，账户内金额不足")
#                     input("按下0：返回主菜单：")
#                     break
#             if(cmd == "0"):
#                 s = 0
#     else:
#         print("帐号或者密码错误")
#         i += 1
# print("===end===")


# continue
# s = 1
# i = 1
# while (i <= 3 and s == 1):
#     name = input("请输入你的帐号：")
#     password = input("请输入你的密码：")
#     if (name == "张三" and password == "123456"):
#         print("登录成功")
#         while(1):
#             print("主菜单：1、查询余额 2、转账 3、取款 0、退出系统")
#             cmd = input("请输入要进行的操作：")
#             if (cmd == "1"):
#                 print("您的账户余额是0")
#                 input("按下0：返回主菜单:")
#                 continue
#             elif (cmd == "2"):
#                 transfer_account = input("请输入要转账的账户：")
#                 trasfer_money = input("请输入要转账的金额：")
#                 print("转账失败，账户内金额不足")
#                 input("0：返回主菜单：")
#                 continue
#             elif (cmd == "3"):
#                 draw = input("请输入要取款的金额：")
#                 print("取款失败，账户内金额不足")
#                 input("按下0：返回主菜单：")
#                 continue
#             elif(cmd == "0"):
#                 s = 0
#                 break
#     else:
#         print("帐号或者密码错误")
#         i += 1
# print("===end===")

# i = 0
# while i < 6:
#     i += 1
#     if(i == 4):
#         continue
#     print(i)
# while +else语句
# i = 1
# while(i < 13):
#     print("111")
#     i += 1
#     if i == 3:
#         break
# else:
#     print("hehe")


s = 1
i = 1
while (i <= 3):
    if(s==0):
        break
    name = input("请输入你的帐号：")
    password = input("请输入你的密码：")
    if (name == "张三" and password == "123456"):
        print("登录成功")
        while(i <= 3):
            print("主菜单：1、查询余额 2、转账 3、取款 0、退出系统")
            cmd = input("请输入要进行的操作：")
            if (cmd == "1"):
                print("您的账户余额是0")
                input("按下0：返回主菜单:")
                continue
            elif (cmd == "2"):
                transfer_account = input("请输入要转账的账户：")
                trasfer_money = input("请输入要转账的金额：")
                print("转账失败，账户内金额不足")
                input("0：返回主菜单：")
                continue
            elif (cmd == "3"):
                draw = input("请输入要取款的金额：")
                print("取款失败，账户内金额不足")
                input("按下0：返回主菜单：")
                continue
            elif(cmd == "0"):
                s = 0
                break
    else:
        print("帐号或者密码错误")
        i += 1
else:
    print("密码输入次数超过3次，不允许再次登录")
print("===系统退出===")
