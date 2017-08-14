#!/usr/bin/env python3
# sum of even valued fib terms
def fib(x):
    a, b = 1, 0
    while a < x:
        yield a
        a, b = b, b+a

print(sum(filter(lambda x: x % 2 == 0, fib(4000000))))