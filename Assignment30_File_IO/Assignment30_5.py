import os

def isWordPresent(fileName, searchWord):
    if os.path.isfile(fileName)==False:
        print("File does not exist in current directory")
        return False

    with open(fileName, "r") as fileObj:
        for line in fileObj:
            if searchWord in line.split():
                print(searchWord)
                return True

    return False


def main():
    fileName = input("Enter file name: ")
    searchWord = input("Enter word to search: ")

    if isWordPresent(fileName, searchWord):
        print(f'Word "{searchWord}" is present in file')
    else:
        print(f'Word "{searchWord}" is NOT present in file')


if __name__ == "__main__":
    main()
