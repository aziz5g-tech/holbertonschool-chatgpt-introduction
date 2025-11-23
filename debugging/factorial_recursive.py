#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial will be calculated.

    Returns:
        int: The factorial value of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
