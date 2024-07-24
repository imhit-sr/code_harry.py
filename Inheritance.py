# >>>>>>Day 61(Inheritance in python)<<<<<<

# When a class derives from the another class
# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def showdetails(self):
#         print(f"The name of Employee:{self.id} is {self.name}")

# class programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python")
    

# e1 = Employee("Rohan Das",456)
# e1.showdetails()
# e2 = programmer("Harryi",785)
# e2.showdetails()
# e2.showLanguage()


# # >>>>>Day 78(Single Inheritance in Python)<<<<
# # Single inheritance is a concept in object-oriented programming where a class (child class)
# # inherits attributes and methods from only one other class (parent class).
# class animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print("Sound made by the animal")


# class Dog(animal):
#     def __init__(self,name,breed):
#         animal.__init__(self,name,species = "Dog")

#         self.breed = breed
#     def __str__(self):
#         return f"The Name is {self.name} with breed {self.breed}"
    
#     def make_sound(self):
#         print("Bark!!")


# a = Dog("VIki","German_shep")
# print(a)
# a.make_sound()

# >>>>Day 79(Multiple Inheritance in python)
# Multiple inheritance is a feature in object-oriented programming where a class (child class) can
# inherit attributes and methods from more than one parent class
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print(f"{self.name} makes a sound.")


# class Owner:
#     def __init__(self, owner):
#         self.owner = owner

#     def show_owner(self):
#         print(f"The owner of this pet is {self.owner}.")

# class Dog(Owner,Animal):
#     def __init__(self, name, breed, owner):
#         Animal.__init__(self, name, species="Dog")
#         Owner.__init__(self, owner)
#         self.breed = breed

#     def __str__(self):
#         return f"The Name is {self.name}, breed is {self.breed}, and owner is {self.owner}"
    
#     def make_sound(self):
#         print("Bark!!")

# # Creating an instance of Dog
# a = Dog("Viki", "German Shepherd", "Alice")
# print(a)             
# a.make_sound()        
# a.show_owner()

# print(Dog.mro())
#Method resolution Order is the order in which python looks for a method or a attribute 
# in a hierarchy(refers to the way classes are organized based on inheritance) of classes

# >>>>Day 80(Multilevel Inheritance in Python)<<<<<
# class LivingBeing:
#     def __init__(self, name):
#         self.name = name

#     def breathe(self):
#         return "Breathing..."

# class Animal(LivingBeing):
#     def __init__(self, name, species):
#         super().__init__(name)  # Call the constructor of LivingBeing
#         self.species = species

#     def eat(self):
#         return "Eating..."

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, species="Dog")  # Call the constructor of Animal
#         self.breed = breed

#     def bark(self):
#         return "Bark!"

# # Creating an instance of Dog
# my_dog = Dog(name="Buddy", breed="Golden Retriever")

# # Using methods from each class
# print(my_dog.name)         # From LivingBeing
# print(my_dog.species)      # From Animal
# print(Dog.mro())

#>>>>> Day 81(Hybrid and Heirerchical Inheritance in python )<<<<<<

# Hybrid Inheritance is a combination of multiple Inheritance and 
# single inheritance in oops

# Example of Hybrid Inheritance         <<<<<<<<< |_|>>>>>>>>>>>>
                                    #  |_|                      |_|
                                        # >>>>>>  # |_|<<<<<<<<<
# class Baseclass:
#     pass

# class Derived1(Baseclass):
#     pass
# class Derived2(Baseclass):
#     pass

# class Derived3(Derived1,Derived2):
#     pass



# Heirarchy 
# CEO
#   |
# -----------
# |   |   |
# m1 m2 m3
# then ass managers

# # Heirarchical Inheritance 
# class Baseclass:
#     pass 

# class D1(Baseclass):
#     pass

# class D2(Baseclass):
#     pass
# class D3(D1):
#     pass
# # chalta jayega