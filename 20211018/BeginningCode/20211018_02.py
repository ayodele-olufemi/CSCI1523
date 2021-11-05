'''
Program: 20211018_02.py
Author: Ayodele Olufemi
Date: 10/18/2021
Purpose: Implement a dictionary relating hexadecimal number to digital number and implement some conversions
'''

hexToBinaryTable = {	'0':'0000', '1':'0001', '2':'0010',
			'3':'0011', '4':'0100', '5':'0101',
			'6':'0110', '7':'0111', '8':'1000',
			'9':'1001', 'A':'1010', 'B':'1011',
			'C':'1100', 'D':'1101', 'E':'1110',
			'F':'1111'}

def convert(number, table):
	'''Builds and returns the base two representation of number. '''
	binary = ""
	for digit in number: 
		binary = table[digit] + binary
	return binary, number

print(convert("35A", hexToBinaryTable))
