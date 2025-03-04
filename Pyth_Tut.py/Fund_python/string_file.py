# In python, anything that you enclose between single or double quotation 
# marks is considered a string.
# >>>>>Basic String<<<<<<
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# # Above is the method to write an multiple line string

# name = "Harry"
# friend = "Rohan"
# anotherFriend = 'Lovish'
# apple = '''He said, 
# Hi Harry
# hey I am good
# "I want to eat an apple'''

# print(name[0])
# print(name[1])

# >>>>>String Slicing<<<<<

# fruit = "Mango "
# mangoLen = len(fruit)
# print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
# print(fruit[len(fruit)-3:len(fruit) - 1])
# print(fruit[-3:-1])

# >>>>String methods in python<<<<<

# l1 = ""
# print(dir(l1))
# Strings are immutable
a = "  !!!Harry!!    !!!!!!!!! Harry  "
# print(len(a))
# print(a.__len__())

# print(a.upper())

# print(a.lower())

# print(a.strip()) #removes the white spaces before and after the string

# print(a.rstrip("Harry"))# the rstrip() removes any trailing characters

# print(a.replace("Harry", "John"))

# print(a.split(" ")) #converts string to list

# blogHeading = "introduction tO jS"
# print(blogHeading.capitalize())

# str1 = "Welcome to the Console!!!"   # The Centre method aligns the string to the centre
# print(str1.center(50))

# print(a.count("Harry"))

# print(str1.endswith("!!!"))
# print(str1.startswith("Welcome"))

# str1 = "Hes name is Dan He is an honest man"
# # print(str1.find("is")) #index also works same
# str = "WelcomeToTheConsole4567"
# print(str.isalnum())

# str1 = "Welcome"
# print(str1.isalpha())

# str1 = "hello world"
# print(str1.islower())


# str1 = "        "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())


# str1 = "World Health Organization" #Returns true if the first word of the entire string is capital

# print(str1.istitle())
# # str1 = "He's name is Dan. Dan is an honest man."
# # print(str1.title())

# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())