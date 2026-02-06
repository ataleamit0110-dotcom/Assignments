import os
import hashlib

def calculateChecksum(filePath):
    hashObj = hashlib.md5()

    with open(filePath, "rb") as fileObj:
        while True:
            data = fileObj.read(1024)
            if not data:
                break
            hashObj.update(data)

    return hashObj.hexdigest()


def displayDirectoryChecksum(directoryName):
    if not os.path.isdir(directoryName):
        print("Directory does not exist")
        return

    print(f"Checksums of files in directory: {directoryName}\n")

    for file in os.listdir(directoryName):
        filePath = os.path.join(directoryName, file)

        if os.path.isfile(filePath):
            checksum = calculateChecksum(filePath)
            print(f"{file}  ->  {checksum}")


def main():
    directoryName = input("Enter directory name: ")
    displayDirectoryChecksum(directoryName)


if __name__ == "__main__":
    main()
