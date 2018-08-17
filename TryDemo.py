import  logging
def foo(s):
    try:
        a =10 / int(s)
    except Exception as e:
        logging.exception('error:',e)
    finally:
        print('end')

if __name__ == '__main__':
    foo('2')
    # 测试try.. except..finally..
    foo('a')