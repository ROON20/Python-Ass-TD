data = input("Enter some data to write to the file: ")
with open("file_name.txt", "w") as file:
    file.write(data)

add_data = input("Enter additional data to append to the file: ")
with open("file_name.txt", "w") as file:
    file.write(add_data)
with open("file_name.txt", "r") as file:
    for line in file:
        print(line.strip())
