class Student(object):
    #相当于java的构造函数，self 是第一个参数，实例化对象的时候，不需要传入self参数
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def _toString(self):
        print('%s:%s' % (self.name,self.score))
    
    def get_grade(self):
        if self.score>=90:
           print('A')
        elif self.score>=60:
           print('B')
        else:
           print('C')


if __name__=='__main__':
    d = Student('d',90)
    d._toString()
    d.get_grade()
        