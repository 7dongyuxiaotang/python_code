# # 1、引用计数
# x = 10
# print(id(x)) #直接引用
# l=['a',x]
# print(id(l[1])) #间接引用
# d={"mmm":x,"nnn":20}
# print(id(d["mmm"])) #间接引用
# y=x  #直接引用
# z=x #直接引用  x的引用次数为5

# 与用户相互
# # 在Python3：input会将用户输入的所有内容都存成字符串类型
# username=input("请输入你的帐号:")
# print(type(username))
# age = input("请输入你的年龄：")
# age = int(age)
# print(age > 16)


# 格式化输出
# ret = "my nanme is %s my age is %d my height is %lf" % ("sss", 38,56)
# print(ret)
# res = "我的名字是%(name)s，你的帐号是%(password)d" % {"password":545854,"name":"张三"}
# print(res)

# %s可以接收任意类型
# print("my name is %s" %18)
# print("my name is %s" %[1,2,3])
# print("my name is %(a)s" %{"a":333})
# print("my name is %d" %18)
# print("my name is %d" %"18")

# res="我的名字是{},我的年龄是{}".format("张三",18)
# print(res)
# res="我的名字是{name},我的年龄是{age}".format(age=18,name="张三")
# print(res)

# f
# x=input("u name:")
# y=input("u age:")
# ret=f"我的名字是{x},我的年龄是{y}"
# print(ret)
# x = input("u name:")
# y = input("u age:")
# ret="我的名字是{x},我的年龄是{y}".format(x = input("u name:"),y = input("u age:"))
# print(ret)


# 1、算数运算符
# print(10+3.1)   13.1
# print(10+3)     13
# print(10/3)     3.3333333333
# print(10//3)    3    保留整数
# print(10 % 3)   1    取模
# print(10**3)    1000 次方

# 2、比较运算符
# print(10 > 3)
# print(10 == 10)
# print(10 >= 3)
# print(10 != 3)


# 解压赋值
# aaa=[111,222,333,444,555,666]
# a1,a2,a3,a4,a5,a6 =aaa
# print(a1,a2,a3,a4,a5,a6)
# aaa=[111,222,333,444,555,666]
# a1,*_,a3=aaa
# print(a1,a3,_)

# 可变不可变类型
# 可变类型：值改变，id不变，证明改的是原值
# 列表是可变类型
# l=["a", "b", "c"]
# print(id(l))
# l[0]="d"
# print(id(l))
# 不可变类型：值改变，id也改变了，证明是产生了新的值
# int 是不可变类型
# x=10
# print(id(x))
# x=11
# print(id(x))
# float 是不可变类型
# x=10.3
# print(id(x))
# x=11.5
# print(id(x))
# str 是不可变类型

