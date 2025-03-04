# >>>>>>>>>Day 65(Static Methods)<<<<<<<<
# Static Methods are the methods that belongs to the Class rather than the 
# instance of the class, so they are called on the class not on the instance
# class student:
#     @staticmethod
#     def add(a,b,c):
#         return (a*b)/c
# result = student.add(2,6,8)
# print(result)



# A Class Method is a method that is bound to the class and
# not the instance of the class,They are defined using the "@classmethod" decorator, 
# The first argument of the function defined is cls which represent the class itself
# class Employee:
#     company = "Apple"
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"The Name is {self.name} and company is {self.company}")
    

#     def changeCompany(cls,newcompany): # The argument cls or first arguments is taken as the object
#         cls.company = newcompany
# e = Employee("Mhiire")
# e.show()
# e.changeCompany("motorsports")
# e.show()
# print(Employee.company)
#If i want to change theclass Employee:
# class Employee:
#     company = "Apple"
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"The Name is {self.name} and company is {self.company}")
    
#     @classmethod
#     def changeCompany(cls,newcompany): # The argument cls or first arguments is taken as the object
#         cls.company = newcompany
# e = Employee("Mhiire")
# e.show()
# e.changeCompany("motorsports")
# e.show()
# print(Employee.company)
#  Python follows a specific lookup order to find the attribute:

# Instance Attributes: It first looks for an attribute named company in the instance (self).
# Class Attributes: If the instance does not have an attribute named company, it then looks for the attribute in the class.
 
# >>>>>>Day 70(Class Methods as Alternative Constructors)<<<<<<
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
# string = "Harry-12000"
# e = Employee(string.split("-")[0],string.split("-")[1])
# print(f"{e.name} and {e.salary}")

# # Above Code is not good and seems not that effective as of split 
# # used while calling the function

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     @classmethod
#     def change(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
        
    
# string = "Harry-12000"
# e = Employee.change(string)
# print(f"{e.name} and {e.salary}")