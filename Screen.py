class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height
    #装饰器@score.setter，负责把一个setter方法变成属性赋值
    @height.setter
    def height(self,value):
        self._height=value
    #只读属性，把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def resolution(self):
        return 786432
    pass