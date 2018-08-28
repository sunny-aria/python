class Student(object):
    def __init__(self,name):
        self._name=name
    def __call__(self, *args, **kwargs):
        print(self._name)


s = Student('hd')
s() #调用call 函数
#使用callable()函数判断一个对象是不是callable对象
print(callable(s))
print(callable([1,2,3]))