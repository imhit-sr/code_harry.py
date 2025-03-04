# Function caching is a technique for improving the performance of a program by
# storing the results of a function call so that you can reuse the results instead of
# recomputing them every time the function is called

import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))
# Output: 6765