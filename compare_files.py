def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        
        content1 = f1.read()
        content2 = f2.read()

        
        if content1 == content2:
            return True
        else:
            return False

file1=input("Enter the path of original file:")
file2=input("Enter the path of retrieved file:")

if compare_files(file1, file2):
    print("The files have the same contents.")
else:
    print("The files have different contents.")
