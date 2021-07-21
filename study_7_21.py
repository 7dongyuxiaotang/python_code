# class Student:
#     stu_school = '广东技术师范大学'
#
#     def __init__(self, massage, name, goal):
#         self.stu_course = massage
#         self.stu_name = name
#         self.stu_goal = goal
#
#
# egon = Student('PE', 'lili', 78)
#
# print(egon.__dict__)
# print(egon.stu_school)

class School:
    school_name = '广师大'

    def __init__(self, address, nickname):
        self.address = address
        self.nickname = nickname
        self.classes = []

    def related_class(self, class_obj):
        self.classes.append(class_obj)

    def tell_class(self):
        print(f'{self.nickname}:')
        for class_obj in self.classes:
            class_obj.tell_course()


# 创建学校
School_While = School('白云', '白云校区')
School_East = School('天河', '东校区')


# # 为学校开设班级
# # 白云校区开设了python课程
# School_While.related_class('python全栈课程')
# School_While.related_class('C语言')
# School_While.related_class('C++')
#
# # 东校区开设了爬虫课程
# School_East.related_class('crawler课程')
# School_East.related_class('Java课程')


#
# # 查看每个校区开设的班级
# School_While.tell_class()
# School_East.tell_class()


class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    def related_course(self, course_obj):
        self.course = course_obj

    def tell_course(self):
        print('班级名称:%s ' % self.name)
        self.course.tell_info()


# 创建班级
class_computer1 = Class('18计算机1班')
class_computer2 = Class('19计算机2班')

# 修改课程
class_computer1.related_course('C++')
class_computer2.related_course('Java课程')

# 为学校开设班级
# 白云校区开设了python课程
School_While.related_class(class_computer1)
# School_While.related_class('C语言')
# School_While.related_class('C++')

# 东校区开设了爬虫课程
School_East.related_class(class_computer2)
# School_East.related_class('Java课程')
# School_While.tell_class()
#
# School_East.tell_class()


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        print('<课程名称:[%s] 周期:[%s] 价钱:[%s]>' % (self.name, self.period, self.price))


# 3、创建课程
course_obj1 = Course('python课程', '6个月', 20000)
course_obj2 = Course('linux运维', '5个月', 10000)

class_computer1.related_course(course_obj1)
class_computer2.related_course(course_obj2)

# class_computer1.tell_course()
School_While.tell_class()


class Student:
    pass
