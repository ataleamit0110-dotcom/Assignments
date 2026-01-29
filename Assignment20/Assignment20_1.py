# Q1. Design a Python application that creates two separate threads named Even and Odd.
# Requirements:
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently.
# Use the threading module.


import threading
import time

def evenNumbers(no):
    for i in range(1, no + 1):
        if i % 2 == 0:
            print(f"Even Thread: {i}")
           # time.sleep(0.5)

def oddNumbers(no):
    for i in range(1, no + 1):
        if i % 2 != 0:
            print(f"Odd Thread: {i}")



def main():
    Value = 10#int(input("Enter number: "))

    T1 = threading.Thread(target=evenNumbers, args=(Value,))
    T2 = threading.Thread(target=oddNumbers, args=(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("Exit from main")


if __name__ == "__main__":
    main()


# Even Thread: 2
# Even Thread: 4
# Odd Thread: 1
# Even Thread: 6
# Even Thread: 8
# Even Thread: 10
# Odd Thread: 3
# Odd Thread: 5
# Odd Thread: 7
# Odd Thread: 9