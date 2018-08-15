'测试private，python使用__ or _ 代表私有属性，不希望被外面访问'

__author__='hd'

def _private_1(name):
	print('hello _private_1 %s' % name)

def _private_2(name):
    print('hello _private_2 %s' % name)	


def test(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)    

if __name__=='__main__':
	test('pyt')