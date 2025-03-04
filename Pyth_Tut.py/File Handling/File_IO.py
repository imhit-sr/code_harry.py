# python provides the open() for opening a File
# It takes two arguments the one is the file name and 
# other is the mode in which file need to be opened    

# f = open("myfile.txt","r")
# text = f.read()
# print(text)
# f.close()
# The Mode is 'r' for reading,'w' for writing and 'a' for appending
# The r mode is default if no argument is given and throughs
# an error if file doesnot exist
# The write(w) mode opens the file for writing only and creates one 
# if it does not exist it removes the initial contents and then write
# whereas append creates the file for append only and creates if doesnot exist



# f1 = open("myfile.txt","w")
# f1.write("Hey bro this is it and it is the same")
# f1.close()


# rb,wb and ab is used to handle binary files like images,pdfs
#  an error if file doesnot exist
# append mode appends to the initial content of the file

# f1 = open("myfile.txt","a")
# f1.write("Hey bro this is it and it is the same")
# f1.close()

# Alternatively We can use with it automatically closes the FileExistsError
# with open("myfile.txt","a") as f:
#     f.write("Hew I am Inside with")