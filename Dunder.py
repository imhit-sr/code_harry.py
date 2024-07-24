
#>>>>> Day 73(Magic/Dunder Methods in python)<<<<<<
# Magic methods, also known as “dunders” from the double underscores
# surrounding their names, are powerful tools that allow you to customize the
# behaviour of your classes. They are used to implement special methods
# such as the addition, subtraction and comparison operators
# , as well as some more advanced techniques like descriptors and properties.


# __init__ # This is the special method that is invoked automatically when an instance
# # of the class is created
# str and repr are both used to convert an object to a string representation
# ,str is used when you want to print out an object,while repr is used when you want a 
# string representation to be used to recreate the object
# class Employee:
#     def __init__(self,name):
#         self.name =  name
    
#     def __len__(self):
#         return len(self.name)
#     def __str__(self):
#         return f"The name of the employee is {self.name}"
#     def __repr__(self):
#         return f"The name of the employee is known as {self.name}"  
#     def __call__(self): #The __call__ method allows an instance of a class to be called as if it were a function
#         return "hey i am nice how are you?"
# a = Employee("Nai_mehtu")
# print(str(a))
# print(repr(a))
# print(a())



