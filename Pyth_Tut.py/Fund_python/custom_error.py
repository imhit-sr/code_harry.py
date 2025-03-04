# Raising Custom Errors in Python
a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise ValueError("Value should be between 5 and 9")
 



# In Python, we can define custom exceptions by creating a new class that is
# derived from the built-in Exception class.

# class CustomError(Exception):
#   # code ...
#   pass
# try:
#   # code ...
# except CustomError:
#   # code...

