
# >>>>>>>>Day 66(Instance vs Class Variables in python)<<<<<<<
# Class Variables
# Class Variables are defined at the class level and can be shared
# among all the instance of the class, also they are accessed from the class
# name only
# When we say a class variable is "shared among all instances of the class," it means that there is 
# # only one copy of that variable, and all instances of the class refer to and modify that same copy. 
# class Myclass:
#     class_var = 0

#     def __init__(self):
#         Myclass.class_var += 1
    
#     def print(self):
#         print(Myclass.class_var)


# obj = Myclass()
# obj1 = Myclass()
# obj2 = Myclass()
# obj2.print()
# # Instance Variable are defined at the instance level and are unique
# # to each instance of the class.
# class Myclass:
#     def __init__(self,name):
#         self.name = name
    
#     def print(self):
#         print(f"{self.name}")

# a = Myclass("Mhiir")
# a.print()


# Attributes vs instance variable vs methods
# Attributes are variables that belong to a class and are used to store information about an object.
# Instance variables are attributes that are specific to each instance of a class.
# Methods: Functions in a class that can access and manipulate instance variables