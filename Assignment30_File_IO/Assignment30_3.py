
import os
def displayFileLineByLine(fileName):
    if os.path.exists(fileName) == False:
        print("File does not exist in current directory")
        return
    
    count = 0
    with open(fileName, "r") as fileObj:
        for line in fileObj:
           print(line)


def main():
    fileName = input("Enter the file name: ")
    displayFileLineByLine(fileName)


if __name__ == "__main__":
   main()
