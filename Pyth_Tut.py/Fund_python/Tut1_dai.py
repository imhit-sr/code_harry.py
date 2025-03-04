
# a = ['freshman', 'sopho', 'junior', 'senior']
# print(list(enumerate(a, 2019)))


# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# # Intersection (&) - Common elements
# print(A & B)  # Output: {3, 4}

# # Union (|) - All unique elements
# print(A | B)  # Output: {1, 2, 3, 4, 5, 6}

# squares = (x**2 for x in range(1, 1001))
# print(type(squares))  # <class 'generator'>


# print({x:x*x for x in range(1,100)})


print(45//4)  #It divides a by b and rounds the result down to the nearest integer.

y = "stuff;thing;junk;"
print(y.split(";"))

# Dictionary built-in Python data type can be used as a hash table?

# List built-in Python data type is best suited for implementing a queue

# wb+ is the mode of both writing and reading in binary format in file4

# dict.get(key, default_value)
# key → The key to look for.
# default_value (optional) → Value to return if key does not exist (default is None).


# x = {'a':'b','c':'d'}
# x.pop('c')
# print(x)

# To move the file cursor to a specific position is the func of seek()

#  To apply the lambda function to all elements of an iterable
# we use map() and filter() in python..

# nums = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x % 2 == 0, nums))
# print(result)

# Q.24 What is the output of the following code?
# from collections import deque
# d = deque([1, 2, 3, 4, 5], maxlen=5)
# d.appendleft(0)
# d.append(6)
# print(d)
# (a) deque([1, 2, 3, 4, 5, 0, 6])
# (b) deque([0, 1, 2, 3, 4, 6])
# (c) deque([0, 1, 2, 3, 4, 5])
# (d) None
# Answer: (d) deque([1, 2, 3, 4, 6], maxlen=5)

# func = lambda x:return x
# pritn(func(2))

# sorted() returns a new list, while .sort() modifies the original list

# Q.27 What is the output when you run the code?
# from functools import reduce
# numbers = [1, 2, 3,4,5,6]
# reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 6))))
# (a) 20
# (b) 40
# (c) 10
# (d) 30

# Q.28 Consider the following list as an input: numbers = [1, 2, 3] Which of the following
# would produce the result: [2] Select all that apply:
# (a) list(filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers))
# (b) list(filter(lambda x: x > 1, numbers))
# (c) list(filter(lambda x: 2, numbers))
# (d) list(filter(lambda x: x % 2 == 0, numbers))


# Q. 29 What is the output of the following code?
# with open('test.txt', 'w+') as f:
#  f.write('Hello\nWorld')
#  f.seek(0)
#  print(f.read(5))
#  print(f.tell())
# a) Hello 5 b) Hello 0 c) Hell 4 d) Hello 10
# Answer: (a)

# Q.30 What is the purpose of the __iter__() method in a custom iterator class?
# a) To initialize the iterator
# b) To return the next item in the iteration
# c) To return the iterator object itself
# d) To signal the end of iteration


# Q.31 Which of the following is not a characteristic of a stack?
# a) LIFO (Last In First Out)
# b) Push operation adds an element
# c) Pop operation removes the most recently added element
# d) Elements can be accessed in any order

# Q.33 Which of the following is not a valid queue operation?
# (a) Enqueue
# (b) Dequeue
# (c) Peek
# (d) Sort

# Q.34 What is the purpose of the 'with' statement when working with files?
# (a) To create a new file
# (b) To ensure the file is properly closed after operations
# (c) To read the entire file at once
# (d) To write to multiple files simultaneously
# Answer: (b)

# Q.38 Which of the following string methods returns a new string with the first character of
# each word capitalized?
# (a) capitalize()
# (b) title()
# (c) upper()
# (d) swapcase()
# Answer: (b)

# Q.40 Which of the following string methods would you use to split a string into a list,
# keeping the delimiters?
# a) split()
# b) partition()
# c) re.split()
# d) splitlines()
# Answer: c)


