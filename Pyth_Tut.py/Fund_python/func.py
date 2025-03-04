# A function is a block of code that performs a specific task whenever it is called.

# There are two types of func, one is built-in-func(min,max,print,list) and other is user-defined func
# def calculateGmean(a, b):
#   mean = (a*b)/(a+b)
#   return mean
# def isGreater(a, b):
#   if(a>b):
#     print("First number is greater")
#   else:
#     print("Second number is greater or equal")

# a = 9
# b = 8
  
# print(calculateGmean(a, b))
# isGreater(7, 3)
# 
# There are four types of arguments that we can provide in a function:

#>>>> Default Arguments<<<<<<
# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
# name("Amy")

    #>>>>> Keyword Arguments<<<<<<
# We can provide arguments with key = value
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name(mname = "Peter", lname = "Wesker", fname = "Jade")


    # >>>>>>Variable length Arguments<<<<<<
# def ret(*name,**fame):
#     print(f"The positional arg are {name}")
#     print(f"The Keyword arg are {fame}")
# ret(4,5,6,1, u = 5,y =6,g = 5)

# >>>>># positional Arguments<<<<<<<
# if we are not using keyword argument we should provide arg 
# with correct positional order
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Ego", "Quill")


# The return statement is used to return the value of the expression back to the calling function.


# func = lambda x:x**2
# print(func(3))

# def compute(num):
#   if num==1:
#     return 1
#   else:
#     return num+compute(num-1)
  
# print(compute(10))


# Problem of gcd and fibonacci

import random

print(random.randint(1,10))


a = ['freshman','sopho','junior','senior']

print(list(enumerate(a,2019)))