'''
Program: 20211018_01.py
Author: Ayodele Olufemi
Date: 10/18/2021
Purpose: 
'''

# Open the file and create a file object f
fileName = input("Enter the file name: ")
f = open(fileName, 'r')

# Input the text, convert it to numbers, and 
# add the numbers to a list

numbers = []

for line in f: 
	words = line.split()
	for word in words: 
		numbers.append(float(word))

# Sort the list and print the number at its midpoint
numbers.sort()

midpoint = len(numbers) // 2
print("The median is ", end=" ")
if len(numbers) % 2 == 1:
	print(numbers[midpoint])
else: 
	print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

av = sum(numbers) / len(numbers)
print(av)
