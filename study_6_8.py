# rt模式
# with open(r'D:\text.txt', mode='rt', encoding='utf-8') as f1:
#     ...
# inp_username = input('请输入您的用户名：').strip()
# inp_password = input('请输入您的密码：').strip()
# with open(r'D:\text.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         username, password = line.strip().split(':')
#         if inp_username == username and inp_password == password:
#             print('登录成功')
#             break
#     else:
#         print('登录失败')


#  wt模式，只写模式

# with open(r'D:\new_file.txt',mode='wt',encoding='utf-8') as f:
#     f.write('hahahahaha\n')
#     f.write('hahahahaha\n')
#     f.write('hahahahaha\n')

# with open(r'D:\new_file.txt',mode='wt',encoding='utf-8') as f:
#     f.write('hahahahaha1\n')
# with open(r'D:\new_file.txt',mode='wt',encoding='utf-8') as f:
#     f.write('hahahahaha2\n')
# with open(r'D:\new_file.txt',mode='wt',encoding='utf-8') as f:
#     f.write('hahahahaha3\n')


#a模式的案例
# inp_name=input("请输入你的用户名：")
# inp_psw=input("请输入你的密码：")
# with open(r'D:\user.txt',mode='at',encoding='utf-8') as f:
#     f.write('{}:{}\n'.format(inp_name,inp_psw))

#w模式的案例
# src_files=input("源文件绝对路径：").strip()
# dst_files=input("新文件绝对路径：").strip()
# with open(r'{}'.format(src_files),mode='rt',encoding='utf-8') as f,\
#     open(r'{}'.format(dst_files),mode='wt',encoding='utf-8') as f2:
#     ret=f.read()
#     f2.write(ret)