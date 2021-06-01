# not 就是把紧跟其后的那个条件取反
# not与把紧跟其后的那个条件是一个不可分割的整体
# print(not 16 > 3)
# print(not 0)

# and  逻辑与 用来链接左右两个条件  有假则假
# print(True and 10>3 and 4==4)
# or:逻辑或  用来链接左右两个条件  有真则真
# print(False or 10<3 or 4==4)
# print(0 or 3 > 2)
# print( (3>4 and (not 4>3)) or (1==3 and 'x'=='x') or 3>3)
# print( 3>4 and not 4>3 or 1==3 and 'x'=='x' or 3>3)

# 成员运算符
# print("GUPN" in "GUPN NB!!!")


# if判断
# 语法1：if 条件:
# i = 60
# if i>60:
#     print("haha")
# elif 20<i<60:
#     print("heihei")
# else:
#     print("hehe")
# 查成绩的小程序
# score=input("请输入你的成绩：")
# score = int(score)
# if (score<60 and score>0):
#     print("不合格")
# elif (score<=80):
#     print("合格")
# elif (score<=100):
#     print("优秀")
# else:  
#     print("请正确输入成绩")

# list1=['egon','lxx',[1,2]]
# list2=list1
# list1[0]='ni'
# print(list2[0])
# print(id(list2))
# print(id(list1))

# list1=['egon','lxx',[1,2]]
# list2=list1.copy()
# print(id(list2[0]))
# print(id(list1[0]))
# list1[0]=555
# list1[2][0]=111
# list1[2][1]=222
# print(list2[2][0])
# print(list2[0])
# list1=[1,2,3,[4,5]]
# list2=list1.copy()
# list1[0]=6
# print(list2[0])
# list1[3][0]=7
# print(list2[3][0])

