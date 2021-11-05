'''
Program: 20211101_02
Author: Ayodele Olufemi
Date: 11/01/2021
Purpose: Graphically illustrate a random walk using Turtle Graphics
'''

from turtle import Turtle
import random

def randomWalk(t, turns, distance = 20):
	for count in range(turns):
			degrees = random.randint(0,270)
			if count % 2 == 0:
				t.left(degrees)
			else:
				t.right(degrees)
			t.forward(distance//random.randint(1,6))

def main():
	t = Turtle()
	t.shape("turtle")
	randomWalk(t,40,100)
	y = input("Press ENTER to continue...")

if __name__ == "__main__":
	main()
