# >>>>>Day 74(Method Overriding in python)<<<<<<
# Method overriding in Python allows you to redefine a method in a 
# derived (child) class that already exists in its base (parent) class.
# class Shape:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
    
#   def area(self):
#       return self.x * self.y

# class Circle(Shape):
#     def __init__(self, radius):
#       self.radius = radius
#       super().__init__(radius, radius)

#     def area(self):
#         return 3.14 *  super().area()
      
# # rec = Shape(3, 5)
# # print(rec.area())

# c = Circle(5)
# print(c.area())