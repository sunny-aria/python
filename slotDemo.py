class slotDemo(object):
    '__slots__ 使用tuple 限制这个类只能绑定这些属性名称'
    __slots__ = ('name','age')

    # def __init__(self,name,age):
    #     #     self.name=name
    #     #     self.age=age

    def __str__(self):
        print(self.name,':',self.age)

# demo = slotDemo(name='hd',age1=18)
demo = slotDemo()
demo.name='hd'
demo.age1 =19 #测试__slots__
demo.__str__()
