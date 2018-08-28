class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path,item))

    def __str__(self):
        return self._path

    __repr__=__str__

#链式调用，每次都进行拼装
print(Chain().status.user.timeline.list)
