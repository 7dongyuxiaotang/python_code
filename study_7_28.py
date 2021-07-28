# class A:
#     def test(self):
#         print('From A')
#         super().test()
#
#
# class B:
#     def test(self):
#         print('From B')
#
#
# class C(A, B):
#     pass
#
#
# obj = C()
# print(A.mro())
# obj.test()


# class Animal:  # 同一类事物:动物
# #     def talk(self):
# #         pass
# #
# #
# # class Cat(Animal):  # 动物的形态之一:猫
# #     def talk(self):
# #         print('喵喵喵')
# #
# #
# # class Dog(Animal):  # 动物的形态之二:狗
# #     def talk(self):
# #         print('汪汪汪')
# #
# #
# # class Pig(Animal):  # 动物的形态之三:猪
# #     def talk(self):
# #         print('哼哼哼')
# #
# #
# # # 实例化得到三个对象
# # cat = Cat()
# # dog = Dog()
# # pig = Pig()


# class Animal:
#     def say(self):
#         print('动物发声的规律.....')
#
#
# class People(Animal):
#     def say(self):
#         print('达咩达咩')
#
#
# class Dog(Animal):
#     def say(self):
#         print('汪汪汪')
#
#
# class Cat(Animal):
#     def say(self):
#         print('喵喵喵')
#
#
# def say(obj):
#     obj.say()
#
#
# obj1 = People()
# obj2 = Dog()
# obj3 = Cat()
#
# say(obj1)
# say(obj2)
# say(obj3)
#
# print(len('hello'))
# print(len([1, 2, 3, 4, 5, 6]))
# print(len({'1': 1, '2': 2}))


class Mysql:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def from_conf(cls):
        return Mysql(setting.IP, setting.PORT)

