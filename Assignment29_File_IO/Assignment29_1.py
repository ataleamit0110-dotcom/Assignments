import os

def main():
    fileName = input("Enter the file name to read: ")

    if os.path.isfile(fileName):
        print("File exists in current directory")
    else:
        print("File does not exist in current directory")

if __name__ == "__main__":
    main()
