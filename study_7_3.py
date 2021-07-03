import json

# #序列化
# dumps_res=json.dumps([1,'aaa',True,False])
# print(dumps_res,type(dumps_res))

# #反序列化
# loads_res=json.loads(dumps_res)
# print(loads_res,type(loads_res))

# dumps_res=json.dumps([1,'aaa',True,False])
# with open(r'D:\python\text.txt',mode='wt',encoding='UTF-8') as f:
#     f.write(dumps_res)

# with open(r'D:\python\text.txt',mode='rt',encoding='UTF-8') as f:
#     loads_res=f.read()
#     l=json.loads(loads_res)
#     print(l)


# import json
# import ujson


# def monkey_patch_json():
#     json.__name__ = 'ujson'
#     json.dumps = ujson.dumps
#     json.loads = ujson.loads


# monkey_patch_json()  # 在入口文件处运行


# import pickle
# res=pickle.dumps({1,2,3,5,6})
# print(res,type(res))


# import configparser

# confi=configparser.ConfigParser()
# confi.read(r'D:\python\text.ini')

# #获取sections
# print(confi.sections())

# #获取某个section下的所有options
# print(confi.options('section1'))

# #获取items
# print(confi.items('section1'))

# #
# print(confi.get('section1','user'))


import hashlib
from re import sub

# m = hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res = m.hexdigest()
# print(res)


# m1 = hashlib.md5()
# m1.update('he'.encode('utf-8'))
# m1.update('llo'.encode('utf-8'))
# m1.update('world'.encode('utf-8'))
# ret = m1.hexdigest()
# print(ret)


# m='A20080306qwer'
# m_md5=hashlib.md5(m.encode('utf-8'))
# m_m='f4921bfc59d1c4b1ba09b38a2e122716'

# passwds=[
#     'E1996325FGHY',
#     'A20080306qwer',
#     '2000306asdf',
#     'qwer20080306A',
#     'A16669852cyem'
# ]


# dir={}
# for p in passwds:
#     res=hashlib.md5(p.encode('utf-8'))
#     dir[p]=res.hexdigest()

# # print(dir)
# for k,v in dir.items():
#     if v == m_m:
#         print('撞库成功，密码是%s'%k)
#         break
    

# import subprocess

# obj=subprocess.Popen(r'D:\python\text.ini',shell=True,
# stdout=subprocess.PIPE,
# stderr=subprocess.PIPE)


# err_obj=obj.stderr.read()
# print(err_obj.decode('gbk'))


