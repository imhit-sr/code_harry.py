
# >>>>>Day 59(Decorators in python)<<<<<
# A decorator is a function that takes another function as an argument and
# returns a new function that modifies the behavior of the original function.


# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for using this app")
#     return mfx

# # @greet
# def hello():
#     print("Hello Siri")
# # hello()
# greet(hello)()

# def func(*args,**kwargs):
#     print(f"Keyword Argument is: {kwargs}")
#     print(f"Postitional Argument is: {args}")

# func(3,4,7,7,f = 4,j=9,e=5)
# import logging
# # Set up basic configuration for logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# def log_fun_call(func):
#     def decorated(*args,**kwargs):
#         logging.info(f"Calling {func.__name__} with args = {args},kwargs = {kwargs}")
#         result = func(*args,**kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result 
#     return decorated 


# @log_fun_call
# def my_func(a,b):
#     return a+b

# my_func(5,6)

