def copyFile(sourceFile, destFile):
    with open(sourceFile, 'rb') as sFileObj, open(destFile, 'wb') as dFileObj:
        
        while True:
            print("Copying...")
            data = sFileObj.read(2) # 1 KB at a time
            print(data)
            if not data:
                break
            dFileObj.write(data)
        
def main():
    sourceFile = input("Enter the source file name: ")
    destFile = input("Enter the destination file name: ")
    copyFile(sourceFile, destFile)
    
    
    
if __name__ == "__main__":
    main()