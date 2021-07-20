# 先定义类 驼峰体
class Student:
    # 1、变量的定义
    stu_school = 'PUBG'

    def __init__(self, name, age, gender, course):
        self.stu_name = name
        self.stu_age = age
        self.stu_gender = gender
        self.sut_course = course

    # 2、 功能的定义

    def tell_stu_info(self):
        pass

    def set_info(self):
        pass

    def choose(self, course):
        self.sut_course = course

    # print(stu_school)


# #1、访问数据属性
# print(Student.stu_school)
# #2、访问函数属性
# print(Student.tell_stu_info(11))

# def init(obj, name, age, gender):
#     obj.stu_name = name
#     obj.stu_age = age
#     obj.stu_gender = gender
#
#
# stu1 = Student()
# init(stu1, 'egon', 18, 'male')
#
# print(stu1.__dict__)
# stu1 = Student()
# stu1.stu_name = '张三'
# print(stu1.__dict__)


# 解决方案二:
obj1 = Student('egon', 18, 'male', '')
obj2 = Student('lili', 18, 'female', '')
obj3 = Student('dsb', 18, 'male', '')
# print(obj1.__dict__)

# print(id(obj1.stu_school))
# print(id(obj2.stu_school))
# print(id(obj3.stu_school))

# Student.stu_school = 'white cloud'
# obj1.stu_school = 'white cloud'
# print(obj1.stu_school)
# print(Student.stu_school)
# print(obj2.stu_school)
obj1.choose('python')
print(obj1.__dict__)

