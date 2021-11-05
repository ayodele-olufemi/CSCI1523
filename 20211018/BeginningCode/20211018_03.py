'''
Program: 20211018_03.py
Author: Ayodele Olufemi
Date: 10/18/2021
Purpose: Introduce functions and the use of __main__ function signature
'''

def main():
	'''The main function for this script.'''
	number = float(input("Enter a number: "))
	result = square(number)
	print("The square of ", number, " is ", result)

def square(x):
	'''Returns the square of x.'''
	return x * x

# The entry point for program execution 
if __name__ == "__main__":
	main()
