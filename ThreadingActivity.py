import time
from threading import Thread

# Creating two empty lists to hold the messages
# and amount to delay each thread from closing
Msgs = []
Dlys = []

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

def msgfunc(i, msgs, dlys):
    time.sleep(int(dlys[i]))
    print(Msgs[i])

def threadStart(isCustom):
    # An IF statement to check if the user has opted to use
    # their own messages, or just see what's happening with
    # the Threads
    if isCustom == 2:
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
    elif isCustom == 1:
        for i in range(len(Msgs)):
            # Creates a new Thread Object, assigned to "t",
            # the thread will run the "myfunc" function, parsing
            # the "i" varible as an argument, and using the messages and
            # delays in the function
            t = Thread(target=msgfunc, args=(i, Msgs, Dlys))
            # Starts the Thread using the the target and
            # arguments in the "Thread" object
            t.start()

def menu():
    ans = input("Would You Like Use Custom Messages[1], or just see Thread Activity[2]?: ")
    if ans == "1":  
        # For loop that asks the user to enter messages, and the amount
        # time to delay each thread
        for i in range(10):
            Msgs.insert(i, input("Please Enter Message Number %s to Display: " % i))
            Dlys.insert(i, input("Please Enter The Number Of Seconds This Thread Should Run: "))

        threadStart(1)
    elif ans == "2":
        threadStart(2)

menu()
