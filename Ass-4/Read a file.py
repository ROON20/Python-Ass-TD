import os

file_name = input("Enter the file name: ")

print("Reading file content: ")

if os.path.exists(file_name):

    print(f"this is a {file_name} file.")

    f = open(file_name, "r")
    aa = f.readline()
    print(aa)
    f.close()
else:
    print(f"The file {file_name} was not found.")
    
