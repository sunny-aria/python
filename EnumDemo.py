from enum import Enum
'Enum 测试'
class Gender(Enum):
    Female =1
    Male=0

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender = gender

bar = Student('jd',Gender.Male)
if bar.gender ==Gender.Female:
    print('测试通过！')
else:
    print("测试失败！")
print(bar.gender)
