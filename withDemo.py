class withDemo(object):
    def __enter__(self):
        print('__in__enter()')
        return 'this is a with demo'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__in__exit()')

class Sample():
    def __enter__(self):
        print("in enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print( "type:",exc_type)
        print( "val:",exc_val)
        print( "tab:",exc_tb)

    def do_something(self):
        bar =1 /0
        return bar+10

with withDemo() as f ,Sample() as f2:
    print('hello:%s'% f)
    f2.do_something()