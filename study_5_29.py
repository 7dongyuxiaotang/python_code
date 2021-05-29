# x = 10
# y = x
# z = x
# del x  # 解除变量名x与值10的绑定关系，10的引用计数变为2
# # print(x)
# print(y)
# print(z)
# # z=1324 再次赋值也可以使得引用计数减少


# 命名风格:
# 1. 纯小写加下划线
# age_of_alex = 73
# print(age_of_alex)
# # 2. 驼峰体
# AgeOfAlex = 73
# print(AgeOfAlex)

# 变量值三个重要特征
# name ='GPNU'
# id:反映的是变量值的内存地址，内存地址不同id则不同
# print(id(name))
# type:不同类型的值用来表示不同的状态
# print(type(name))
# value:变量本身
# print(name)

# is 与 ==
# is 比较左右两边变量id是否相等
# x = 'YUE'
# y = 'YUE'
# print(id(x), id(y))
# print(x == y)

# 小整数池：从python解释器启动那一刻开始，就会在内存中事先申请好一系列内存空间存放好常用的整数
# n = 10
# m = 10
# ret = 4+6
# print(id(n))
# print(id(m))
# print(id(ret))

# n = 156398235658
# m = 156398235658
# print(id(n))
# print(id(m))

# 注意：python语法中没有常量的概念，但是在程序的开发过程中会涉及到常量的概念
# AGE_OF_ALEX = 73 小写字母全为大写代表常量，这只是一个约定、规范

# age=18
# print(type(age))
# weight=55.3
# print(type(weight))

# name="赛利亚"
# name2='赛利亚'
# name3='''赛利亚'''
# print(type(name))
# print(type(name2))
# print(type(name3))
# print(name)
# print(name2)
# print(name3)

# 字符串的嵌套，注意：外层用单引号 \ 双引号，内层用双引号 \ 单引号
# print('my name is"sailiya"')
# print("my name is'sailiya'")

# x = "my name is "
# y = "赛利亚"
# print(x+y)
# print(id(x))
# print(id(y))
# print(id(x+y))

# print('='*20)
# print("hallo world")
# print('='*20)


# 列表：索引对应值，索引从0开始，0代表第一个
# 作用：记录多个值，并且可以按照索引取指定位置的值
# 定义：在[]内用逗号分割开多个任意类型的值，一个值称之为一个元素
# l=[10,3.1,'aaa',["aaa","bbb"],"ccc"]
# print(l[3][0])
# print(l[-1])

#字典
# key对应值，其中key通常为字符串类型，所以key对值可以有描述性的功能
# 作用：用来存多个值，每一个值都有唯一一个key与其对应。
# 定义：在{ }内用逗号分开各多个key:value
# d={'a':1 , 'b':2,'c':6}
# print(d['c'])
# student_info=[
#     {"name":"张三","age":19,"sex":"男"},
#     {"name":"李四","age":20,"sex":"女"},
#     {"name":"王五","age":39,"sex":"保密"}
# ]
# print(student_info[2]["sex"])

