# import socket
# 基于tcp协议
# # 1、买手机
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 流式协议=》tcp协议
#
# # 2、绑定手机卡
# phone.bind(('127.0.0.1', 8080))
#
# # 3、开机
# phone.listen(5)  # 5指的是半连接池的大小
#
# # 4、等待电话链接请求
#
#
# # 5、收消息
# while True:
#     conn, client_addr = phone.accept()
#     print(conn)
#     print('客户端的ip和端口：', client_addr)
#     while True:
#         try:
#             data = conn.recv(1024)  # 最大接收的数据量为1024Bytes,收到是bytes类型
#             if len(data) == 0:
#                 break
#             if data.decode('utf-8') == 'quit':
#                 break
#             print('客户端发来的消息：', data.decode('utf-8'))
#             conn.send(data.upper())
#         except Exception:
#             break
#
#     # 6、关闭电连接conn
#     conn.close()
#
# # 7、关机(可选操作)
# phone.close()

# 基于udp协议
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 数据报协议=>udp协议

server.bind(('127.0.0.1', 8080))

while True:
    data, client_addr = server.recvfrom(1024)
    if data.decode('utf-8') == 'quit':
        break
    print('客户端传递的信息:', data.decode('utf-8'))
    server.sendto(data.upper(), client_addr)

server.close()
