
def filesAreEqual(file1, file2):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        while True:
            data1 = f1.read(10)
            data2 = f2.read(10)
            print(data1)
            print(data2)
            if data1 != data2:
                return False

            if not data1:  # both reached EOF
                return True


def main():
    firstFile = input("Enter the first file name: ")
    secondFile = input("Enter the second file name: ")
    isEquql = filesAreEqual(firstFile, secondFile)
    if isEquql:
        print("Both files are equql")
    else:
        print("Files are not equql")

if __name__ == "__main__":
   main()
