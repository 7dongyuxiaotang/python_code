# 注册功能 用户输入帐号密码，按照'egon:18'存入文件
# inp_name=input('请输入你要使用的用户名：').strip()
# inp_pwd=input('请输入你要使用的密码：').strip()
# with open(r'D:\user_message.txt',mode='at',encoding='utf-8') as f:
#     f.write('{}:{}\n'.format(inp_name,inp_pwd))
# print('注册成功')

# 基于上述注册信息，完成登录验证
# inp_name=input('请输入你的用户名：').strip()
# inp_pwd=input('请输入你的密码：').strip()
# with open(r'D:\user_message.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         username,userpassword=line.strip().split(':')
#         print(username)
#         if username==inp_name and userpassword ==inp_pwd:
#             print('登录成功')
#             break
#     else:
#         print('登录失败')

# 旧文件内容复制到新文件
# old_files=input('请输入你要复制的文件地址：').strip()
# new_files=input('请输入你要粘贴到的文件地址：').strip()
# with open(r'{}'.format(old_files),mode='rt',encoding='utf-8') as f,\
#     open(r'{}'.format(new_files),mode='wt',encoding='utf-8') as f2:
#     ret=f.read()
#     f2.write(ret)

# with open(r'D:\x模式.txt',mode='xt',encoding='utf-8') as f:
#     f.write('哈哈哈哈哈')

# with open(r'D:\配送中心.png',mode='rb') as ret:
#     f=ret.read()

# with open(r'D:\text.txt',mode='wb') as f:
#     f.write('哈哈哈'.encode('utf-8'))


# 文件复制
# old_files=input('请输入你要复制的文件地址：').strip()
# new_files=input('请输入你要粘贴到的文件地址：').strip()
# with open(r'{}'.format(old_files),mode='rb') as f,\
#     open(r'{}'.format(new_files),mode='wb') as f2:
#     for line in f:
#         f2.write(line)


# 循环读取文件
# 方式一：自己控制每次读取的数据的数据量
# with open(r'test.txt',mode='rb') as f:
#     while True:
#         res=f.read(1024)#一次读取1024个字节
#         if len(res) == 0:
#             break
#         print(len(res))

# 方式二：以行为单位读，当一个内容过长时会导致一次性读入内容的数据量过大
# with open(r'test.txt',mode='rb') as f:
#   for len in f:
#       print(len(line),line)


# with open(r'D:\user_message.txt', mode='rt', encoding='utf-8') as f:
#     ret = f.readlines()
#     print(ret)


# writelines
# with open(r'D:\user_message.txt', mode='wt', encoding='utf-8') as f:
#     f.writelines(['111','222','333'])

#read(n)
# with open(r'D:\user_message.txt', mode='rt', encoding='utf-8') as f:
#     ret=f.read(6)
#     print(ret)

# with open(r'D:\user_message.txt', mode='rt', encoding='utf-8') as f:
#     f.seek(3,0)
#     res=f.tell()
#     ret=f.read()
#     print(ret)
#     print(res)