import os
def main():
    directoryName = input("Enter the directory name: ")
    extensionFirst = input("Enter the first file extension : ")
    extensionSecond = input("Enter the second file extension : ")

    displayAllFileWithExtension(directoryName, extensionFirst, extensionSecond)


def displayAllFileWithExtension(directoryName, extension1, extension2):
    if os.path.exists(directoryName) == False:
        print("Directory does not exist in current directory")
        return
    
    for file in os.listdir(directoryName):
        print("filess",file)
        if file.endswith(extension1):
            os.rename(
                os.path.join(directoryName, file),
                os.path.join(directoryName, file.replace(extension1, extension2))
            )



if __name__ == "__main__":
    main()

