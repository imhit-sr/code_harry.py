# # >>>>>>Day 71(dir,dict and help methods in oops)<<<<<
#  The dir() function returns a list of all the attributes and methods (including dunder methods) available
# for an object. It is a useful tool for discovering what you can do with an object
# x = [1, 2, 3]
# print(dir(x))

# x = [1, 2, 3]
# y = [4, 5, 6]
# print(x + y)  
# print(x.__add__(y))  

# The __dict__ attribute returns a dictionary representation of an object's attributes
# class Person:
#   def __init__(self, name, age):
#       self.name = name

#       self.age = age
#       self.version = 1

    
# p = Person("John", 30)
# print(p.__dict__)
# # he help() function is used to get help documentation for an object, including a description of its attributes and methods
# print(help(Person))