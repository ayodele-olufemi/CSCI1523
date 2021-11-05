'''
File: 20211011_01.py
Author: Ayodele Olufemi
Date: 10/11/21
Purpose: Encrypts an input string of the ASCII character and prints the result. The other input is the distance value.
'''

# The ASCII values range from 0 to 127

plainText = input("Enter a message: ")
distance = int(input("Enter a distance value: "))

code = ""

for ch in plainText: 
	ordValue = ord(ch)
	cipherValue = ordValue + distance
	if cipherValue > 127:
		cipherValue = distance - (127 - ordValue + 1)
	code += chr(cipherValue)
print(code)
