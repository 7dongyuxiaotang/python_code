# msg="Hello world"
# res=msg[::-1]
# print(res)

# 去掉字符串两边的需要去除的字符
# msg = "   He   llo   "
# ret = msg.strip()
# print(ret)

# 切分：把一个字符串按照某种分割符按照某种分隔符进行切分，得到一个列表
# msg="name:18:male:student:paly basketball"
# ret=msg.split(":")
# print(ret)
# print(retr)
# print("+".join(ret))

# 替换字符串：
# msg="name:18:male:student:paly basketball:name"
# print(msg.replace("name","张三",1))

# 判断这个字符串中是否是纯数字
# int_str ="123456789"
# int_str1="123456789."
# print(int_str.isdigit())
# print(int_str1.isdigit())

# find、index返回要查找的字符串在大字符串中的起始索引
# msg="name:18:male:student:paly basketball:name"
# print(msg.find("student"))
# msg="name:18:male:student:paly basketball:name"
# print(msg.index("student"))
# print(msg.index("xxx"))

# count 统计字符出现的次数
# msg="name:18:male:student:paly basketball:name"
# print(msg.count("name"))
# print("student".center(50,"*"))
# print("student".ljust(50,"*"))
# print("student".rjust(50,"*"))
# print("student".zfill(50))
# print(msg.expandtabs(1))
# msg="name 18 male student paly basketball name"
# print(msg.capitalize())
# print(msg.swapcase())
# print(msg.title())

# 类型转换：但反能够被for循环遍历的类型都可以当做参数传给list( )转成列表
# res=list("hello")
# print(res)
# msg=list({"k1":111,"k2":222,"k3":333})
# print(msg)


# l=[111,"hello","play basketball"]
# 正向取
# print(l[0])
# #反向取
# print(l[-1])
# #可以取可以改
# l[0]=222
# print(l[0])

# append 列表追加
# l.append(3333)
# print(l)
# #insert 列表插入
# l.insert(1,222)
# print(l)

# #列表追加到列表
# l=[111,"hello","play basketball"]
# l2=[222,333,"hehe",555]
# l.extend(l2)
# print(l)

# 列表删除值
# l = [111, "hello", "play basketball"]
# ret = l.pop(1)
# print(ret)
# print(l)
# l.remove("hello")
# print(l)


#列表求长度，元素个数
# l = [111, "hello", "play basketball"]
# print(len(l))


#count
# l = [111, "hello", "play basketball"]
# print(l.count("hello"))
#clear
# l.clear()
# print(l)
#index()
# print(l.index("hello"))
#reverse
# l.reverse()
# print(l)
#sort
# l=[5,9,3,2,-6,8]
# l.sort(reverse=True) #默认为False,升序。True,降序
# print(l)


#元组
# t=(111,222,"hello")
# print(t,type(t))
# t=(10,[11,22])
# print(id(t[0]),id(t[1]))
# t[1][0]="hehe"
# print(t)
# print(id(t[0]),id(t[1]))

#字典
# d={"k1":111,2:222,(1,2):333}
# print(d["k1"])
# print(d[(1,2)])
# print(type(d))
#字典的类型转换
# info=[["name","张三"],["age",18],["gender","male"]]
# d={}
# for item in info:
#     d[item[0]]=item[1]
# print(d)
# ret=dict(info)
# print(ret)
# keys=["name","age","gender"]
# values=None
# d={}.fromkeys(keys,values)
# print(d)

#字典优先掌握的操作
# d={"k1":111,"k2":222}
# d["k3"]=333
# print(d)
# d={"k1":111,"k2":222,"k1":333,"k1":444}
# print(len(d))
# print(d)
# ret=d.pop("k1")
# print(d)
# print(ret)
# d={"k1":111,"k2":222,"k3":333,"k4":444,"k5":555,"k6":666}
# ret=d.popitem()
# print(d)
# print(ret)
# print(d.keys())
# print(d.values())
# print(d.items())
# d.update({"k1":"hehe","k7":777})
# print(d)
# print(d.get("k7"))
# set=d.setdefault("k7",777)
# print(d)
# print(set)