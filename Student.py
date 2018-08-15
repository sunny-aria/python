class Student(object):
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
        _toString()

        