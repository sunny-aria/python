from functools import reduce

'python raise demo'

__author__='hd'

def str2num(s):
    return int(s)

def calc(exp):
    ss=exp.split('+')

    ns = map(str2num,ss)

    return reduce(lambda x,y:x+y,ns)

if __name__ == '__main__':
    try:
        # r=calc('100+200+30.0')
        r=calc('100+200+300')
        print('100+200+300=',r)
    except Exception as e:
        print('error:',e)
        # 抛出异常
        raise e
    pass