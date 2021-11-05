'''
Program: 20211025_01
Author: Ayodele Olufemi
Date: 10/25/2021
Purpose: Illustrate to use of functions in a python script
'''

def repToInt(repString, base = 2):
	decimal = 0
	exponent = len(repString) - 1
	for digit in repString:
		decimal = decimal + int(digit) * base ** exponent
		exponent = exponent - 1
	return decimal

def example(required, option1 = 2, option2 = 3):
	print(required, option1, option2)
	return required, option1, option2

# Exercise a default formal parameter function 
i,j,k = example(6,23,34)

# First try a conversion
print(repToInt('64', 8))


# Multiple values returned
print(example(23, 24, 25))

print(i,j,k)
