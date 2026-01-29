# Q4. Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should:
# Count and display the number of lowercase characters.
# The Capital thread should:
# Count and display the number of uppercase characters.
# The Digits thread should:
# Count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# Thread Name

import threading

def CountSmall(strData):
    count = 0
    thread = threading.current_thread()
    print("\nThread Name:", thread.name)
    print("Thread ID:", thread.ident)

    for ch in strData:
        if ch.islower():
            count += 1

    print("Number of lowercase characters:", count)


def CountCapital(strData):
    count = 0
    thread = threading.current_thread()
    print("\nThread Name:", thread.name)
    print("Thread ID:", thread.ident)

    for ch in strData:
        if ch.isupper():
            count += 1

    print("Number of uppercase characters:", count)


def CountDigits(strData):
    count = 0
    thread = threading.current_thread()
    print("\nThread Name:", thread.name)
    print("Thread ID:", thread.ident)

    for ch in strData:
        if ch.isdigit():
            count += 1

    print("Number of digits:", count)


def main():
    strData = input("Enter a string: ")

    T1 = threading.Thread(target=CountSmall, args=(strData,))
    T2 = threading.Thread(target=CountCapital, args=(strData,))
    T3 = threading.Thread(target=CountDigits, args=(strData,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()