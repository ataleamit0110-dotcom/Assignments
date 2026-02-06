import os
import hashlib

def getChecksum(filePath):
    hashObj = hashlib.md5()

    with open(filePath, "rb") as fileObj:
        while True:
            data = fileObj.read(1024)
            if not data:
                break
            hashObj.update(data)

    return hashObj.hexdigest()


def findDuplicateFiles(directoryName):
    if not os.path.isdir(directoryName):
        print("Directory does not exist")
        return

    checksumDict = {}

    for file in os.listdir(directoryName):
        filePath = os.path.join(directoryName, file)

        if os.path.isfile(filePath):
            checksum = getChecksum(filePath)

            if checksum in checksumDict:
                checksumDict[checksum].append(file)
            else:
                checksumDict[checksum] = [file]

    with open("log.txt", "w") as logFile:
        logFile.write("Duplicate files found:\n\n")

        found = False
        for checksum, files in checksumDict.items():
            if len(files) > 1:
                found = True
                logFile.write(f"Checksum: {checksum}\n")
                for file in files:
                    logFile.write(f"  {file}\n")
                logFile.write("\n")

        if not found:
            logFile.write("No duplicate files found\n")

    print("Duplicate file names written to log.txt")


def main():
    directoryName = input("Enter directory name: ")
    findDuplicateFiles(directoryName)


if __name__ == "__main__":
    main()
