type()
isinstance(c,object)
class A(object):
    def __init__(self):
        self.x=10


a =A()
dir(a)
# dir() 列出
hasattr(a,'x')
setattr(a,'x',30)
getattr(a,'x')

# 实例属性
# 类属性，相当于java 的static 属性，属于类，所有实例对象共用
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count=Student.count+1