import time
from threading import Thread



def myfunc(i, count):
    print("sleeping 5 sec from thread %d" % i)
    time.sleep(count)
    print("finished sleeping from thread %d" % i)

count = 1

for i in range(10):
    t = Thread(target=myfunc, args=(i, count))
    t.start()
    count += 1