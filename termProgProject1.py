# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:45:29 2021

Program: A program to take input of numbers and calculate their sum and average
Author: Ayodele Olufemi

"""
# First we prompt the user for input of numbers

numberCount = 0
inputNumber = 0
sumOfNumbers = 0

while inputNumber != "": 
    data = input("Enter a number (Leave empty and press 'Enter' key to start computation): ")
    if data == "":
        inputNumber = data
    else:
        try:
            inputNumber = float(data)
            numberCount += 1
            sumOfNumbers += inputNumber
        except ValueError:
            print("Could not convert data to number.")
try:
    print("\n{} numbers were entered. Their sum is {} and their average is {}.".format(numberCount, sumOfNumbers, sumOfNumbers / numberCount))
except ZeroDivisionError:
    print("No number was entered. Average cannot be computed.")
        
    