
# >>>>>>Day 60(Getters and setters in python)<<<<<<
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         self.email = f"{fname}.{lname}@codewitme.com"
#     def explain(self):
#         return f"this employee is {self.fname} {self.lname}"
    
#     def printemail(self):
#         pass


# a = Employee("hi","bye")
# print(a.email)
# a.fname = "bye"
# print(a.email)

# Below approach can reslove this problem

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         self.email = f"{name}.{salary}@codewitme.com"
#     def explain(self):
#         return f"this employee is {self.name} {self.salary}"
    
#     # def printemail(self):
#     #     return f"{self.name}.{self.salary}@codewitme.com"
#     @property
#     def email(self):
#         return f"{self.name}.{self.salary}@codewitme.com"
#     @email.setter
#     def email(self,string):
#         print("Setting now")
#         names = string.split("@")[0]
#         self.name = names.split(".")[0]
#         self.salary = names.split(".")[1]

# a = Employee("sachai","kimurti")
# # a.name = "jaye"
# # print(a.printemail())
# print(a.email)  #a.email is a property, defined using the @property decorator.
# # # Properties are accessed like attributes, without parentheses.
# # # Methods are called with parentheses.
# a.email = "thi.ith@gmail.com"
# # # The email.setter is called when you assign a value to the email property.
# # # In contrast, the @property getter is called when you access the email property. 
# print(a.name)
# print(a.salary)





# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self._balance = balance  # Private attribute to store the balance
    
#     @property
#     def balance(self):
#         """Getter method for balance"""
#         return self._balance
#     @balance.setter
#     def balance(self, amount):
#         """Setter method for balance"""
#         if amount < 0:
#             print("Cannot set a negative balance!")
#         else:
#             self._balance = amount

#     def deposit(self, amount):
#         """Method to deposit money into the account"""
#         if amount <= 0:
#             print("Deposit amount must be positive!")
#         else:
#             self._balance += amount
#             print(f"Deposited {amount}. New balance is {self._balance}.")


#     def withdraw(self, amount):
#         """Method to withdraw money from the account"""
#         if amount > self._balance:
#             print("Insufficient funds!")
#         elif amount <= 0:
#             print("Withdrawal amount must be positive!")
#         else:
#             self._balance -= amount
#             print(f"Withdrew {amount}. New balance is {self._balance}.")


# account = BankAccount("700878640", 3000)

# print(f"Initial balance in  your account is : {account.balance}")

# account.deposit(500)

# account.withdraw(300)
# print(f"Final balance: {account.balance}")