
import os
def numberfOfLines(fileName):
    if os.path.exists(fileName) == False:
        print("File does not exist in current directory")
        return
    
    count = 0
    with open(fileName, "r") as fileObj:
        for line in fileObj:
            count = count + 1
    return count


def main():
    fileName = input("Enter the file name: ")
    result = numberfOfLines(fileName)
    print(f'total lines are: {result}')


if __name__ == "__main__":
   main()
