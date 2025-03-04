def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1
# Each call to yield pauses the function and returns the current count.
# # Using the generator
# # Memory Efficiency: Generators do not store all the values in memory at once. They 
# # generate each value on the fly, making them memory-efficient for large datasets or infinite sequences.
# counter = count_up_to(5)
# print(next(counter))
# print(next(counter))
# # for number in counter:
# #     print(number)


# Storing the entire Fibonacci sequence in a list consumes a lot of memory,
# which can be problematic for large sequences.
def fibonacci_generator():
    """Generate an infinite sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# a and b are not setted to 0,1 because the generator saves its state and continue
# where it left off


# Using the Fibonacci number generator
fib_gen = fibonacci_generator()
for _ in range(100):  # Print the first 10 Fibonacci numbers
    print(next(fib_gen))