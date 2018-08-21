import time,threading

'Thread demo'

def loop():
    print("thread %s is running..." % threading.current_thread().getName())
    n=0
    while n<5:
        n=n+1
        print("thread %s >>> %s" %(threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s ended." % threading.currentThread().name)

print("thread %s is running..." % threading.currentThread().name)

t = threading.Thread(target=loop,name='LoopThread')

t.start()
t.join()
print("thread %s ended."%threading.currentThread().name)