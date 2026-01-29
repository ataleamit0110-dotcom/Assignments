# Q2. Design a Python application that creates two threads to find maximum and minimum element from a list.
# Thread 1 should calculate and display the maximum element.
# Thread 2 should calculate and display the minimum element.
# The list should be accepted from the user.

import threading

def FindMax(arr):
    print("Maximum element:", max(arr))

def FindMin(arr):
    print("Minimum element:", min(arr))

def main():
    arr = list(map(int, input("Enter list: ").split()))

    T1 = threading.Thread(target=FindMax, args=(arr,))
    T2 = threading.Thread(target=FindMin, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()