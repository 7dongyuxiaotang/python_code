# import socket
#
# # 1 、买手机
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 2、拨通电话
# phone.connect(('127.0.0.1', 8080))
#
# # 3、通信
# while True:
#     msg = input("请输入你要发送的信息：").strip()
#     if len(msg) == 0:
#         continue
#     phone.send(msg.encode('utf-8'))
#     if msg == 'quit':
#         break
#     data = phone.recv(1024)
#     print('服务端发送的消息：', data.decode('utf-8'))
#

# # 4、关闭链接
# phone.close()


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('请输入信息：').strip()
    if msg == 'quit':
        break
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
    data, server_addr = client.recvfrom(1024)
    print(data.decode('utf-8'))
client.close()
