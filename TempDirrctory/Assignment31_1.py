import os
def main():
    directoryName = input("Enter the directory name: ")
    extension = input("Enter the extension name: ")
    displayAllFileWithExtension(directoryName, extension)


def displayAllFileWithExtension(directoryName, extension):
    if os.path.exists(directoryName) == False:
        print("Directory does not exist in current directory")
        return
    print(f"Files with extension {extension} in directory {directoryName} are:")
    for folderName, subFolders, fileNames in os.walk(directoryName):
        print(f"Current folder is: {folderName}")
       

    for file in os.listdir(directoryName):
        #print("filess",file)
        if file.endswith(extension):
             print("aaaaa",file)


if __name__ == "__main__":
    main()

