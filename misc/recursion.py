#!/bin/python
def factorial(n):
    # print("Entering: " + str(n))
    if n == 1:
        # print("Exiting: "  + str(n))
        return 1
    result = n*factorial(n-1)
    # print("Exiting: "  + str(n))
    return result

print(factorial(1)==1)
print(factorial(10)==3628800)
print(factorial(5)==120)
print(factorial(8)==40320)

# Print all fibonacci numbers upto n
# fib(n) = fib(n - 1) + fib(n - 2)
def fib(n):
    if n == 0:
        return n
    if n <= 2:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result

print(fib(2) == 1)
print(fib(8) == 21)
print(fib(9) == 34)
