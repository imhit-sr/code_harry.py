
# >>>>>>Day 62(Access Modifiers/Specifiers in python)<<<<<<
# Access Specifiers in python are used to limit the use of class or instance variables
# and class methods outside of the class while implemenenting the concept of inheritance
# Public Access Modifiers
# Can be accessed from anywhere
# class student:
#     def __init__(self,age,name):
#         self.name = name
#         self.age = age
# obj = student(21,"Haui")
# print(obj.age)
# print(obj.name)
#Private Access modifier are those which are accessible only inside the class not in subclass
# we cannot use pv outside of the class
# its not like it cant be accessed but there is convention to use it inside the class

# class student:
#     def __init__(self,age,name):
#         self.__name = name
#         self.__age = age
#     def __info(self,position):
#         print(f"The name is {self.__name} and {self.__age} and {position}")


# class Man(student):
#     def indigo_mind(self):
#         print(f"This is the child class")
# obj = student(21,"Haui")
# obj1 = Man(45,"vikas_mee")
# print(obj1._student__age)

# print(obj.__age)
# print(obj.__name) Cant be accessed using this 
# obj.__info("youtube")
# obj._student__info("youtube")
# print(obj._student__name)
# print(obj._student__age)
# When you declare a variable in a class with two leading 
# underscores, like __name, Python internally changes the variable name to _classname__variablename(This is known as the Name Mangling)
# In your student class, __name becomes _student__name and __age becomes _student__age.
# This makes these variables harder to access from outside the class
# This process is known as the Name Mangling

#Proctected Access Modifier
# Protected variables are intended to be accessed within
# the class and its subclasses, although they can still
#  be accessed from outside if necessary. The leading underscore is a convention to indicate
#  that these variables are meant for internal use.
# class student:
#     def __init__(self,age,name):
#         self._name = name
#         self._age = age
# obj = student(21,"Haui")
# print(obj._name)