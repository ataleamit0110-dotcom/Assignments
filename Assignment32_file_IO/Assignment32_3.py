import os
import hashlib

def getChecksum(filePath):
    hashObj = hashlib.md5()
    with open(filePath, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            hashObj.update(data)
    return hashObj.hexdigest()


def deleteDuplicateFiles(directoryName):
    if not os.path.isdir(directoryName):
        print("Directory does not exist")
        return

    checksumDict = {}

    # Step 1: Build checksum dictionary
    for file in os.listdir(directoryName):
        filePath = os.path.join(directoryName, file)
        if os.path.isfile(filePath):
            checksum = getChecksum(filePath)
            checksumDict.setdefault(checksum, []).append(filePath)

    # Step 2: Create log file in CURRENT directory
    logFilePath = os.path.join(os.getcwd(), "Log.txt")

    with open(logFilePath, "w") as logFile:
        logFile.write("Deleted duplicate files:\n\n")
        found = False

        # Step 3: Delete duplicates
        for checksum, files in checksumDict.items():
            if len(files) > 1:
                found = True
                # Keep first file, delete rest
                for duplicateFile in files[1:]:
                    os.remove(duplicateFile)
                    logFile.write(duplicateFile + "\n")

        if not found:
            logFile.write("No duplicate files found\n")

    print(f"Duplicate files removed. Log created at: {logFilePath}")


def main():
    directoryName = input("Enter directory name: ")
    deleteDuplicateFiles(directoryName)


if __name__ == "__main__":
    main()
