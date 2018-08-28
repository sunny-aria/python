import unittest
# 个人理解,导入Student文件中的Student类
from Student import Student

'''
单元测试demo,
单元测试方法都以test 开头，py才会执行
'''

__author__='浩东'
"""
多行注释，可以用三个三引号，也可以用三个双引号
单元测试要继承 unittest.TestCase
"""
class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('bart',90)
        s2 = Student('lisa',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')

    def test_60_to_80(self):
        s1 = Student('bart',60)
        s2 = Student('Lisa',79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_60_to_80(self):
        s1 = Student('bart',0)
        s2 = Student('Lisa',59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

#main必须靠左
if __name__ == '__main__':
        unittest.main() #执行单元测试，调用main方法执行所有的单元测试方法