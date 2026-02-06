import os
import shutil

def copyDirectory(sourceDir, destDir):
    # Check source directory
    if not os.path.isdir(sourceDir):
        print("Source directory does not exist")
        return

    # Create destination directory if not exists
    if not os.path.exists(destDir):
        os.mkdir(destDir)
        print(f"Directory {destDir} created")

    # Copy all files
    for file in os.listdir(sourceDir):
        sourcePath = os.path.join(sourceDir, file)
        destPath = os.path.join(destDir, file)

        if os.path.isfile(sourcePath):
            shutil.copy(sourcePath, destPath)

    print("All files copied successfully")


def main():
    sourceDir = input("Enter source directory name: ")
    destDir = input("Enter destination directory name: ")

    copyDirectory(sourceDir, destDir)


if __name__ == "__main__":
    main()
