import time,threading

local_thread = threading.local()
'''
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

可以理解为全局变量local_school是一个dict，不但可以用local_school.name，还可以绑定其他变量，如local_school.teacher等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

小结

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''
def process_student():
    #获取当前线程关联的属性
    stu_name = local_thread.name
    print("hello,%s (in %s)." %(stu_name,threading.currentThread().name))


def process_thread(name):
    local_thread.name=name
    process_student()

if __name__ == '__main__':

    t1 = threading.Thread(target=process_thread,args=('haodong1',),name='Hd1-thread')
    t2 = threading.Thread(target=process_thread,args=('haodong2',),name='Hd2-thread')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Thread %s end." % threading.currentThread().name)