"""
This module has the method to calculate factorial of the given number
"""
def factorial(num):
    if num in (0, 1):
        return 1
    return num * factorial(num-1)
print(factorial(5))
