# 4. Design a Python application that creates two threads to compute sum and product of elements from a list.
# Thread 1 should compute the sum of elements.
# Thread 2 should compute the product of elements.
# Return results to the main thread and display them.
import threading

sum_result = 0
product_result = 1

def CalculateSum(arr):
    global sum_result
    for num in arr:
        sum_result = sum_result + num

def CalculateProduct(arr):
    global product_result
    for num in arr:
        product_result = product_result * num

def main():
    arr = list(map(int, input("Enter list: ").split()))

    T1 = threading.Thread(target=CalculateSum, args=(arr,))
    T2 = threading.Thread(target=CalculateProduct, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)

    print("Exit from main")

if __name__ == "__main__":
    main()