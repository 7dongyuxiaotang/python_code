# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print('<%s:%s>' % (self.name, self.age))
#
#
# obj = People('egon', 18)
# print(type(obj))
# print(type(People))
# class_name = 'People'
# class_bases = (object,)
# class_dic = {}
# class_body = '''
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# def say(self):
#     print('<%s:%s>' % (self.name, self.age))
# '''
# exec(class_body, {}, class_dic)
#
# print(class_dic)
#
# People = type(class_name, class_bases, class_dic)
#
# obj = People('egon', 18)
# print(obj.__dict__)


class Mymeta(type):  # 只有继承了type类的类才是元类
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise NameError('类名首字母为大写')
        print('run2')

    def __new__(cls, *args, **kwargs):
        print('run1')
        return super().__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        # 1、Mymeta.__call__函数内调用People内的__new__
        people_obj = self.__new__(self)
        # 2、Mymeta.__call__函数内调用People内的__init__
        self.__init__(people_obj, *args, **kwargs)
        # 3、Mymeta.__call__函数内返回一个初始化好的对象
        return people_obj


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s:%s>' % (self.name, self.age))

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)





obj = People('egon', 18)
print(obj.__dict__)
