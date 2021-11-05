"""
Program: 20211101_01
Author: Warren Sheaffer
Date: 11/10/2021
Purpose: Implements a recursion and prints a trace of a recursive sum function.
"""

def summation(lower, upper, margin = 0):
    """
    Arguments: A lower bound, an upper bound, and the number of
               blanks in the margin
    Returns: the sum of the numbers between the arguments
             and including them
    """
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + summation(lower+1, upper, margin+4)
        print(blanks, result)
        return result

summation(2,4)
