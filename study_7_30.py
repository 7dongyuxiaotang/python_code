class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<%s:%s>' % (self.name, self.age)

    def __del__(self):
        # 发起系统调用，告诉操作系统回收相关的系统资源
        self.x.close()


obj = People('we', 29)
print(obj)
#
# print(hasattr(obj, 'name'))
# print(getattr(obj, 'name'))
# setattr(obj, 'name', 'egon')
# print(getattr(obj, 'name'))


# class Ftp:
#     def put(self):
#         print('正在执行上传功能')
#
#     def get(self):
#         print('正在执行下载功能')
#
#     def interactive(self):
#         method = input('>>>:').strip()
#
#         if hasattr(self, method):
#             getattr(self, method)()
#         else:
#             print('输入的指令不存在')
#
#
# obj = Ftp()
# obj.interactive(
