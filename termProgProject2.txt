'''
Program: A Python program that allows users to navigate the lines of text in a file.
Author: Ayodele Olufemi
Date: 10/16/2021
'''

# Prompting for text file name

fileName = input("Enter the input file name: ")

# Opening the text file
textFile = open(fileName, 'r')

# Creating list object to hold lines of text
linesList = []

# Reading lines from text file
while True:
	line = textFile.readline()
	if line == "":
		break
	linesList.append(line)

# Entering loop to prompt user for line number

while True:
	print(f"There are {len(linesList)} lines of text in the file.")
	try:
		lineNumber = int(input("Enter a line number: "))
		if lineNumber == 0:
			print("Quitting program...")		
			break
		print(linesList[lineNumber - 1])
	except ValueError:
		print("You entered and invalid number.")
	except IndexError:
		print("Line number does not exist.")

# Closing the file
textFile.close()



