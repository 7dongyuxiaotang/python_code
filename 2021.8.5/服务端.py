from socket import *
import socketserver


# import subprocess
# import struct
# import json
#
# server = socket(AF_INET, SOCK_STREAM)
#
# server.bind(('127.0.0.1', 8080))
#
# server.listen(5)
#
# while True:
#     conn, client_address = server.accept()
#
#     while True:
#         try:
#             cmd = conn.recv(1024)
#             if len(cmd) == 0:
#                 break
#             obj = subprocess.Popen(cmd.decode('utf-8'),
#                                    shell=True,
#                                    stdout=subprocess.PIPE,
#                                    stderr=subprocess.PIPE
#                                    )
#             stdout_res = obj.stdout.read()
#             stderr_res = obj.stderr.read()
#             total_size = len(stderr_res) + len(stdout_res)
#
#             # 头部信息
#             header_dic = {
#                 'filename': 'a.txt',
#                 'total_size': 123545687,
#                 'md5': 'asd789a8s7cv46x57a8w'
#             }
#             # 将头部信息写成json格式，可以方便其他平台进行接收
#             json_str = json.dumps(header_dic)
#             json_str_bytes = json_str.encode('utf-8')
#
#             # 将带有头部信息的字典转成固定大小，方便客户端解析，提取头部信息
#             header_size = struct.pack('i', len(json_str_bytes))
#             conn.send(header_size)
#
#             conn.send(json_str_bytes)
#
#             # 2、再发送真实的数据
#             conn.send(stdout_res)
#             conn.send(stderr_res)
#         except Exception:
#             break
#
#     conn.close()


# server = socket(AF_INET, SOCK_STREAM)
#
# server.bind(('127.0.0.1', 8099))
#
# server.listen(5)


# class MyRequestHandle(socketserver.BaseRequestHandler):
#     def handle(self):
#         print(self.request)  # 如果是tcp协议，相当于self.request=>conn
#         print(self.client_address)
#         while True:
#             try:
#                 msg = self.request.recv(1024)
#                 if len(msg) == 0:
#                     break
#                 self.request.send(msg.upper())
#             except Exception:
#                 break
#         self.request.close()


# 服务端应该做两件事情
# 第一件事：循环地从半连接池中取出链接请求与其建立双向链接，拿到链接对象

# s = socketserver.ThreadingTCPServer(('127.0.0.1', 8099), MyRequestHandle)
# s.serve_forever()
# 等同于
# while True:
#   conn,client_address = server.accept()
#   启动一个线程(conn,client_address)

# 第二件事：拿到链接对象，与其进行通信循环====》hanle方法


# 基于udp协议
class MyRequestHanlde(socketserver.BaseRequestHandler):
    def handle(self):
        client_data = self.request[0]
        server = self.request[1]
        client_address = self.client_address
        print('客户端发来的数据：%s' % client_data)
        server.sendto(client_data.upper(), client_address)


s = socketserver.ThreadingUDPServer(('127.0.0.1', 8090), MyRequestHanlde)
s.serve_forever()
