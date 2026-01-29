# .5 Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization.

import threading

def DisplayForward():
    print("Thread1 started")
    for i in range(1, 51):
        print("Thread1:", i)

def DisplayReverse():
    print("Thread2 started")
    for i in range(50, 0, -1):
        print("Thread2:", i)

def main():
    T1 = threading.Thread(target=DisplayForward, name="Thread1")
    T2 = threading.Thread(target=DisplayReverse, name="Thread2")
    # Start Thread1
    T1.start()
    # Wait until Thread1 completes
    T1.join()

    # Start Thread2 only after Thread1 finishes
    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()