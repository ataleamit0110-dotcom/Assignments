
import os
def countOccurrences(fileName, searchText):
    if os.path.exists(fileName) == False:
        print("File does not exist in current directory")
        return
    
    count = 0
    with open(fileName, "r") as fileObj:
        for line in fileObj:
            count += line.count(searchText)
    return count


def main():
    fileName = input("Enter the file name: ")
    searchText = input("Enter the text for searching: ")
    result = countOccurrences(fileName, searchText)
    print(f'Frequency of "{searchText}" is: {result}')


if __name__ == "__main__":
   main()
