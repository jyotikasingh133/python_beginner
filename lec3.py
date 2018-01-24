# File Handling


fo = open("file.txt", "w+")
print("File Name : ", fo.name, "\n mode = ", fo.mode, end=" : ")

if fo.mode == "r":
    print("Opens a file for reading only")
elif fo.mode == "r+":
    print("Opens a file for both reading and writing")
elif fo.mode == "w":
    print("Opens a file for writing only")
elif fo.mode == "w+":
    print("Opens a file for both writing and reading")
elif fo.mode == "a":
    print("Opens a file for appending.")
elif fo.mode == "a+":
    print("Opens a file for appending and reading.")

if fo.mode == "a" or fo.mode == "a+":
    print("The file pointer is at the end of the file if the file exists.")
    print("If file does not exists, create new file otherwise append the file.")
else:
    print("The file pointer is at the beginning of the file if the file exists.")
    if fo.mode == "w" or fo.mode == "w+":
        print("If file does not exists, create new file ")
        print(" otherwise overwrite the existing file")


fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()
