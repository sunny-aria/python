def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2
#测试错误
def main():
    bar('0')
    # print(bar('2'))
if __name__ == '__main__':
    main()