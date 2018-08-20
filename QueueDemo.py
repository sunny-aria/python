from multiprocessing import Process,Queue

import  os,time,random

'进程间通过queue通信'

'''
一个进程负责写队列
'''
def write(q):
    print('Process to wirte:%s' % os.getpid())
    for value in ['a','hd','c']:
        print("Put -%s- to queue..." % value)
        q.put(value)
        time.sleep(random.random())
'''
一个进程负责读队列
'''
def read(q):
    print("Process to read:%s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get =%s= from queue..." % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
