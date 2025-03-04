# The Map,Filter and Reduce are built in functions that allow 
# you to apply a function to a sequence of element and return a new 
# sequence.they are refered to as a higher order function
# as they take other func as an argument

# map(function,iterable)

# cube = lambda x:x**2
# l = [1,2,8,12,13]
# newl = list(map(cube,l))

# print(newl)


# # filter(predictable,iterable)
# # The filter function on a given predicate(a function that return a boolean value)
# # and returns a new sequence containing only the elements that meet the predicate

# # def filter_func(a):
# #     return a>4

# # newnewl = list(filter(filter_func,l))
# # print(newnewl)

# from functools import reduce

# sum = reduce(lambda x,y:x+y/2,l)
# print(sum)