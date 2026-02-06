import os
def main():
    fileName = input("Enter the file name to display contents: ")
    dispalyContent(fileName)
    
def dispalyContent(fileName):
    if os.path.exists(fileName) == False:
        print("File does not exist in current directory")
        return
    with open(fileName, "r") as fileObj:
        for a in fileObj:
            print(a)
    
if __name__ == "__main__":
    main()