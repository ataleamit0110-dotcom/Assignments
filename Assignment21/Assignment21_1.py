# Q1. Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# Prime thread should display all prime numbers from the list.
import threading

def isPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no / 2) + 1):
        if no % i == 0:
            return False
    return True

def DisplayPrime(arr):
    print("Prime thread started")
    for num in arr:
        if isPrime(num):
            print("Prime number:", num)

def DisplayNonPrime(arr):
    print("NonPrime thread started")
    for num in arr:
        if not isPrime(num):
            print("Non-prime number:", num)

def main():
    arr = list(map(int, input("Enter list: ").split()))

    T1 = threading.Thread(target=DisplayPrime, args=(arr,), name="Prime")
    T2 = threading.Thread(target=DisplayNonPrime, args=(arr,), name="NonPrime")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()