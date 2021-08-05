# import json
from socket import *

# import struct
#
# client = socket(AF_INET, SOCK_STREAM)
#
# client.connect(('127.0.0.1', 8080))
#
# while True:
#     msg = input('请输入命令:>>>').strip()
#     if len(msg) == 0:
#         continue
#     if msg == 'quit':
#         break
#         # 接收端，先接收4个字节，从中提取接下来要接收的头的长度
#     header_size = client.recv(4)
#     header_len = struct.unpack('i', header_size)[0]
#     # 提取到了头部长度，就可以接收头部信息字典
#     json_str_bytes = client.recv(header_len)
#     # 将bytes格式转化了json，再转化为utf-8
#     json_str = json_str_bytes.decode('utf-8')
#     header_dic = json.loads(json_str)
#     total_size = header_dic['total_size']
#     recv_size = 0
#     while recv_size < total_size:
#         recv_data = client.recv(1024)
#         recv_size += len(recv_data)
#         print(recv_data.decode('utf-8'))
#
#     client.send(msg.encode('utf-8'))
#     cmd_res = client.recv(1024)
#     print(cmd_res.decode('utf-8'))
#
# client.close()

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8099))

while True:
    msg = input('请输入你的信息：').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode('utf-8'))

    res = client.recv(1024)
    print(res.decode('utf-8'))
