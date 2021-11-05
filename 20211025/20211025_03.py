'''
Program: 20211025_01
Author: Ayodele Olufemi
Date: 10/25/2021
Purpose: Scoping in functions
'''

x = "module"

def f():
	x = "temporary"
	print(x)

print(x)

f()

print(x)


