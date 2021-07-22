# class Foo:
#     __x = 1  # _Foo__x = 1
#
#     def __f1(self):   # _Foo__f1
#         print('hello world')
#
#     def f2(self):
#         print(self.__x)
#         print(self.__f1)
# print(Foo.__dict__)
# print(Foo._Foo__x)
# print(Foo._Foo__f1)

# obj = Foo()
#
# obj.f2()


# class People:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         print(self.__name)
#
#     def set_name(self,val):
#         if type(val) is not str:
#             print('必须传入字符串')
#             return
#         self.__name = val
#
#
# obj = People('egon')
#
# obj.set_name(115)


# class Teacher:
#     def __init__(self, name, age):
#
#         # self.name = name
#         # self.age = age
#         self.set_info(name, age)
#
#     def tell_info(self):
#         print('姓名:%s,年龄:%s' % (self.__name, self.__age))
#
#     def set_info(self, name, age):
#         if not isinstance(name, str):
#             raise TypeError('姓名必须是字符串类型')
#         if not isinstance(age, int):
#             raise TypeError('年龄必须是整型')
#         self.__name = name
#         self.__age = age
#
#
# t = Teacher('egon',18)
# t.tell_info()
#
# t.name  #无法直接使用.name


# class Teacher:
#     def __init__(self, name, age):
#         if not isinstance(name, str):
#             raise TypeError('姓名必须是字符串类型')
#         if not isinstance(age, int):
#             raise TypeError('年龄必须是整型')
#         self.name = name
#         self.age = age
#
#     def tell_info(self):
#         print('姓名:%s,年龄:%s' % (self.name, self.age))
#
#
# t = Teacher('egon', 18)
# t.tell_info()
#
# t.name = 18
# t.age = 'egon'
# t.tell_info()

# 案例一：
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# obj1 = People('egon', 66, 1.5)
# print(obj1.bmi)


# 案例二：
class People:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('姓名必须是字符串类型')
        self.__name = name

    @name.deleter
    def name(self):
        print('不让删除')
        pass


t = People('egon')

t.name = 'haha'
print(t.name)
