'''
File: 20211011_02.py
Author: Ayodele Olufemi
Date: 10/11/21
Purpose: Decrypts an input string of the ASCII character and prints the result. The other input is the distance value.
'''

# The ASCII values range from 0 to 127

code = input("Enter the coded text: ")
distance = int(input("Enter a distance value: "))

plainText = ""

for ch in code: 
	ordValue = ord(ch)
	cipherValue = ordValue - distance
	if cipherValue < 0:
		cipherValue = 127 - (distance - (1 - ordValue))
	plainText += chr(cipherValue)
print(plainText)
