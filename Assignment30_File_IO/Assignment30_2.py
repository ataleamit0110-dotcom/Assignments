
import os
def countWordsInFile(fileName):
    if os.path.exists(fileName) == False:
        print("File does not exist in current directory")
        return
    
    count = 0
    with open(fileName, "r") as fileObj:
        for line in fileObj:
            words = line.split()   # split line into words
            count += len(words) 
    return count


def main():
    fileName = input("Enter the file name: ")
    result = countWordsInFile(fileName)
    print(f'total lines are: {result}')


if __name__ == "__main__":
   main()
