# for x,y,z in ['abc',(1,2,3),["c","d","e"]]:
#     print(x,y,z)

# f=["张三","李四","王五","老六","老七"]
# f2=["王尼玛","张三","赵铁柱","陈胖胖","王五"]
# l=[]
# for x in f:
#     if x in f2:
#         l.append(x)
# print(l)

# s={1,2,3,4,5,1,1,2,1}
# print(s)

# 关系运算
# f = {"张三", "李四", "王五", "老六", "老七"}
# f2 = {"王尼玛", "张三", "赵铁柱", "陈胖胖", "王五"}
# 两者取交集
# print(f & f2)
# 两者取并集
# print(f | f2)
# 取某个集合的差集
# print(f-f2)
# 对称差集
# print(f ^ f2)
# s={1,2,3,4,5,6,7,8,9}
# s1={1,2,3,4}
# print(s>s1)
# print(f.intersection(f2))
# print(f.union(f2))
# print(f.difference(f2))
# print(f.symmetric_difference(f2))
# print(f.issuperset(f2))

#去重
# s=set([1,2,5,6,3,2,[1,2,3,6,5]])
# s=set(["hehe","haha",12,15,"heihei",12,15,"hehe"])
# print(s)

#dicard
# s={1,2,3,4,5,6,7,8,9}
# s.discard(3)
# print(s)

# s={1,2,3,4,5,6,7,8,9}
# s1={1,2,3,4}
# s.difference_update(s1)
# print(s)
# print(s.isdisjoint(s1))
# str="我喜欢你"
# print(str.encode('unicode-escape').decode())

