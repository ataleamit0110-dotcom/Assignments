# Design a Python application that creates two threads named EvenList and OddList.
# Requirements:
# Both threads should accept a list of integers as input.
# The EvenList thread should:
# Extract all even elements from the list.
# Calculate and display the sum of even elements.
# The OddList thread should:
# Extract all odd elements from the list.

import threading

def EvenList(numbers):
    print("EvenList thread started")
    even_sum = 0

    for num in numbers:
        if num % 2 == 0:
            print("Even element:", num)
            even_sum = even_sum + num

    print("Sum of even elements:", even_sum)


def OddList(numbers):
    print("OddList thread started")
    odd_sum = 0

    for num in numbers:
        if num % 2 != 0:
            print("Odd element:", num)
            odd_sum = odd_sum + num

    print("Sum of odd elements:", odd_sum)


def main():
    arr = list(map(int, input("Enter list elements: ").split()))

    T1 = threading.Thread(target=EvenList, args=(arr,))
    T2 = threading.Thread(target=OddList, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()