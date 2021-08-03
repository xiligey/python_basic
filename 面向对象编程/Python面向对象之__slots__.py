"""
__slots__的作用是限制本身及子类属性名称
子类定义的属性是自身的slots加上父类的slots
"""


class Student:
    """学生"""
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class MeritStudent(Student):
    """三好学生"""
    __slots__ = ('grade',)


if __name__ == '__main__':
    student1 = Student()
    student1.name = 'Jack'
    student1.age = 18
    # student1.sex = 'male'  # 加上这行会报错, 因为slots限制了可以添加的属性只有name和age

    student2 = MeritStudent()
    student2.name = 'Rose'
    student2.age = 17
    student2.grade = 100  # 子类定义的属性是自身的slots加上父类的slots
