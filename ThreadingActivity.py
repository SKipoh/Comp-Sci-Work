import time
from threading import Thread

# Declaring a function called "myfunc", that needs a
# variable "i" parsed to it
def myfunc(i):
    # Prints out a statement, using the "i" varible
    # to show the thread number
    print("sleeping 5 sec from thread %d" % i)
    # Sleeps for the amount of time that "i"
    time.sleep(i)
    # Prints a statement telling the user thread for
    # the value of "i" has been closed
    print("finished sleeping from thread %d" % i)

# For loop that iterates 10 times, starting a new thread
# for each time it runs "myfunc", as well as iterating
# the "count" variable
for i in range(10):
    # Creates a new Thread Object, assigned to "t",
    # the thread will run the "myfunc" function, parsing
    # the "i" varible as an argument
    t = Thread(target=myfunc, args=(i,))
    # Starts the Thread using the the target and
    # arguments in the "Thread" object
    t.start()
