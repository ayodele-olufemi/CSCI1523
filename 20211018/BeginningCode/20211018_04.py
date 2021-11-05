'''
Program: 20211018_04.py
Author: Ayodele Olufemi
Datea: 10/18/2021
Purpose: Create a listing of unique words in a text file in alphabetical order.
'''

# Take the input file name
inName = input("Enter the input file name: ")

# Open the input file and initialize list of unique words
inputFile = open(inName, 'r')
uniqueWords = []

# Add the unique words in the file to the list
for line in inputFile:
	words = line.split()
	for word in words:
		if not word in uniqueWords: 
			uniqueWords.append(word)

# Sort the list of unique words 
uniqueWords.sort()

# Print the unique words
for word in uniqueWords: 
	print(word)
