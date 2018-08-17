class Student(object):
    #相当于java的构造函数，self 是第一个参数，实例化对象的时候，不需要传入self参数
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def _toString(self):
        print('%s:%s' % (self.name,self.score))
    
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('成绩不合法', self.score)
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'


if __name__=='__main__':
    d = Student('d',90)
    d._toString()
    d.get_grade()
        