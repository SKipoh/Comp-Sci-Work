import time
from threading import Thread

def myfunc(i):
    print("/nsleeping 5 sec from thread %d" % i)
    time.sleep(5)
    print("/nfinished sleeping from thread %d" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()