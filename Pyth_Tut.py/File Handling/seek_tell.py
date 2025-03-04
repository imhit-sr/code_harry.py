# seek() and tell() functions are used to work with file objects
# and their different positions within a file

# seek() func allows you to move the current position 
# within a file to a specific point and you can move further
# and backward from there 
# tell() returns the current position within the file in bytes
# with open("myfile.txt","r") as f:
#     print(type(f))

#     f.seek(9)
#     print(f.tell())
#     data = f.read(15)
#     print(data)


# truncate function can be used for trancuating the File

# with open("myfile.txt","w") as f:
#     f.write("Hello World and i have to go to there ")
#     # print(type(f))
#     f.truncate(10)
 
# with open("myfile.txt","r") as f:
#     print(f.read())
