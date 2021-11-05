'''
Program: 20211025_02
Author: Ayodele Olufemi
Date: 10/25/2021
Program: Illustrate the use of function, iterative and recursive problem solving
'''

def summation_1(lower, upper):
	"""
	Arguments: A lower bound and upper bound
	Returns: the sum of the numbers between the arguments and including them
	"""
	result = 0
	while lower <= upper: 
		result += lower
		lower += 1
	return result


"""
Prints a trace of a recursive sum function;
"""

def summation_2(lower, upper, margin = 0):
	"""
	Arguments: A lower bound, an upper bound, and the number of blanks in the margin.
	Returns: the sum of the numbers between the arguments and including them
	"""
	blanks = " " * margin
	print(blanks, lower, upper)
	if lower > upper: 
		print(blanks, 0)
		return 0
	else: 
		result = lower + summation_2(lower + 1, upper, margin + 4)
		print(blanks, result)
		return result

print(summation_1(2,5))
print(summation_2(2,5))
