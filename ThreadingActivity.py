import time
import random
from threading import Thread

# Creating two empty lists to hold the messages
# and amount to delay each thread from closing, as
# well as a list of 50 generated words from the Lorum
# Ipsum as "random messages"
Msgs = []
rndMsgs = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur" "adipiscing", "elit", "Quisque" "gravida", "convallis", "ornare", "Aliquam", "vel", "lorem", "a", "lectus", "commodo", "aliquet", "Aenean" "fermentum", "ante", "vitae", "tempor", "tempus", "ipsum", "magna", "mollis", "tellus", "sit", "amet", "bibendum", "lectus", "diam", "ac", "elit", "Fusce", "condimentum", "vitae", "urna", "ac", "sagittis", "Sed", "iaculis", "nunc", "vel", "sollicitudin", "sollicitudin", "Etiam","maximus"]
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

# A new function called "msgfunc", that needs 3 variables parsed
# that are used for counting, the messages to display, and the amount
# to delay, respectively
def msgfunc(i, msgs, dlys):
    # sleep function that sleeps for as long as the integer
    # in the list at location "i"
    time.sleep(int(dlys[i]))
    # Prints out the message at position "i" in the Msgs list
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
    # Asks the user for whether they just want to see when a Thread is opened or closed,
    # use their own messages and timing, or use words from the generated list
    ans = input("Would You Like Use Custom Messages[1], see Thread Activity[2], or use Generated Messages[3]?: ")
    
    # An IF statement used to determine what the user wants to do
    if ans == "1":  
        # For loop that asks the user to enter messages, and the amount
        # time to delay each thread
        for i in range(10):
            Msgs.insert(i, input("Please Enter Message Number %s to Display: " % i))
            Dlys.insert(i, input("Please Enter The Number Of Seconds This Thread Should Run: "))

        # After all the messages and delays have been gathered, run the threadStart function
        # and parse it the value "1"
        threadStart(1)
    elif ans == "2":
        # If the user enters "2", then run threadStart and parse "2"
        threadStart(2)
    elif ans == "3":
        # If the user enters "3", then run threadStart and parse "3"
        threadStart(3)
    elif ans != "1" or ans != "2" or ans != "3":
        # Error handling to see if the input doesn't equal any of these values,
        # then it tells the user, and reloads the menu
        print("Not a valid input!")
        menu()

menu()
