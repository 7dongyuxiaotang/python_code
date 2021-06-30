import random
# print(random.random())
# print(random.randint(1,3))  #[1,3] 随机产生一个1<= and <=3的整数
# print(random.randrange(1,3)) #[1,3) 随机产生一个 1<= and <3的整数
# print(random.choice([1,'aaa',[1,5,6]])) #随机从choice([])中挑选一个值,注意()多个值需要放在列表中
# print(random.sample([1,'22',[1,2,3]],2)) #随机列表挑选N个元素进行组合
# print(random.uniform(1,3)) #随机产生一个 1< and <3的小数
# item=[1,2,3,4,5,6,7,8,9]
# random.shuffle(item)#打乱一个列表里面值的顺序
# print(item)

# # 验证码随机
# def make_code(size=4):
#     res = ''
#     for i in range(size):
#         s1 = chr(random.randint(65, 90))
#         s2 = str(random.randint(0, 9))
#         res += random.choice([s1, s2])
#     return res

# print(make_code())