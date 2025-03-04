# >>>>Day 72(Super Keyword in Python)<<<<<<
# The super() keyword is used to refer to the parent class
# this is used when we want to call a method from the parent class

class Employee:
    def __init__(self,name,company):
        self.name = name
        self.company = company 
    def info_employee(self):
        return f"The person name is {self.name} and company is {self.company}"
    
class Person(Employee):
    def __init__(self,name,company,marital_status,salary):
        self.marital_status = marital_status
        self.salary = salary
        super().__init__(name,company)
    def info_per(self):
        return f"{self.name} and {self.marital_status}"

a = Person("Mihir_bansal","Rizorpay","Unmarried",80000)
print(a.info_per())