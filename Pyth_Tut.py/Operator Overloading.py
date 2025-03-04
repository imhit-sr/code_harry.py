# Operator overloading in Python allows custom behavior for standard operators (+, -, *, etc.) 
# with instances of your classes by defining special methods like __add__, __sub__, and so on

# >>>>>Day 77(Operator Overloading in Python)<<<<<<
# class Vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
    
#     def __add__(self,x):
#         return Vector(self.i + x.i,self.j+x.j,self.k+x.k)

# v = Vector(4,7,1)
# print(v)

# v1 = Vector(4,6,2)
# print(v+v1)
# Docs.python similarly there is __mul__,__sub__ and many more