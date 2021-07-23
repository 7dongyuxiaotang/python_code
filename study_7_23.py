# class Parent1(object):
#     x = 1111
#
#
# class Parent2(object):
#     pass
#
#
# class Sub1(Parent1):  # 单继承
#     pass
#
#
# class Sub2(Parent1, Parent2):  # 多继承
#     pass
#
#
# print(Sub1.x)
# print(Sub1.__bases__)
# print(Sub2.__bases__)

# ps:在python2中有经典类与新式类之分
# 新式类：继承了object类的子类，以及该子类的子类
# 经典：没有继承object类的子类，以及该子类的子类

# ps:在python3中没有继承任何类，默认继承object类
# 所以python3中所有类都是新式类

# class School:
#     school = '广东技术师范大学'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Student(School):
#
#     def choose_course(self):
#         print('%s 正在选课' % self.name)
#
#
# class Teacher(School):
#
#     def __init__(self, name, age, gender, salary, level):
#         School.__init__(self, name, age, gender)
#         self.salary = salary
#         self.level = level
#
#     def score(self):
#         print('%s老师 正在给学生打分' % self.name)


# class Foo:
#
#     def __f1(self):
#         print('foo.f1')
#
#     def f2(self):
#         print('foo.f2')
#         self.__f1()
#
#
# class Bar(Foo):
#
#     def f1(self):
#         print('bar.f1')
#
#
# obj = Bar()
#
# obj.f2()


class A:
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B, C):
    pass


print(D.mro())  # 类以及该类的对象访问属性都是参照该类的mro列表
# obj = D()
# obj.test()
