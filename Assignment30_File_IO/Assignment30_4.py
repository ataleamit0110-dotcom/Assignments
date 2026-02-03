import os

def copyFileLineByLine(sourceFile, destFile):

    if os.path.exists(sourceFile) == False:
        print("Source file does not exist in current directory")
        return
    

    with open(sourceFile, "r") as src, open(destFile, "w") as dest:
        for line in src:
            dest.write(line)

    print("File copied successfully")


def main():
    sourceFile = input("Enter the source file name: ")
    destFile = input("Enter the destination file name: ")

    copyFileLineByLine(sourceFile, destFile)


if __name__ == "__main__":
    main()
