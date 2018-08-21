import time,threading

balance =0

def change_it(n):
    global  balance
    balance = balance+n
    balance = balance-n
#对共享资源加锁
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        lock.acquire()# 申请加锁
        try:
            change_it(n)
        finally:
            lock.release() #释放锁

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)