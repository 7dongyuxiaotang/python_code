# class A(object):
#     def test(self):
#         print('from A')
#
#
# class B(A):
#     # def test(self):
#     #     print('from B')
#     pass
#
#
# class C(A):
#     def test(self):
#         print('from C')
#
#
# class D(B):
#     # def test(self):
#     #     print('from D')
#     pass
#
#
# class E(C):
#     def test(self):
#         print('from E')
#
#
# class F(D, E):
#     # def test(self):
#     #     print('from F')
#     pass
#
#
# f1 = F()
# f1.test()
# # print(F.__mro__)  # 只有新式才有这个属性可以查看线性列表，经典类没有这个属性
#
# # 新式类继承顺序:F->D->B->E->C->A
# # 经典类继承顺序:F->D->B->A->E->C
# # python3中统一都是新式类
# # python2中才分新式类与经典类


# class Vehicle:
#     pass
#
#
# class FlyableMixin:
#     def fly(self):
#         pass
#
#
# class CivilAircraft(FlyableMixin, Vehicle):  # 民航飞机
#     pass
#
#
# class Helicopter(FlyableMixin, Vehicle):  # 直升飞机
#     pass
#
#
# class Car(Vehicle):  # 汽车
#     pass


class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('%s say hello' % self.name)


class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex)

        self.level = level
        self.salary = salary


Teacher1 = Teacher('egon', 18, 'male', 10, 3000)
print(Teacher1.__dict__)
