"""
Program:    termProgProj3
Author:     Ayodele Olufemi
Date:       11/16/2021
Purpose:    A GUI-based program that plays a guess-the-number game
Notes:      The program allows the computer to make an informed RANDOM guess, by using the knowlege of 
            previous guesses. The program could have utilized a binary search, but it won't be random 
            in that case and may be out of the scope of the class. 
            The program could also abstract some operations into methods, but I just decided to make it 
            as simple as possible.
            The program also didnt catch exceptions when users enter non-numbers, 0 , negative numbers
            or numbers greater than 100 as secretNumber
            Also, I showed the guesses for testing purpose
"""

import random
from breezypythongui import EasyFrame


class ComputerGuessGame(EasyFrame):
    """Plays a guessing game with the user."""

    def __init__(self):
        """Setting up the window, widgets and data."""
        EasyFrame.__init__(self, title="Computer Guessing Game")
        # Computer guesses the secret number.
        self.computerGuess = random.randint(1, 100)
        self.tooLargeList = []
        self.tooSmallList = []
        self.count = 0

        self.hintLabel = self.addLabel(
            text="Guess a number between 1 and 100", row=0, column=0, sticky="NSEW", columnspan=2)
        self.addLabel(text="My secret number", row=1, column=0)
        self.mySecretNumber = self.addIntegerField(0, row=1, column=1)
        self.addLabel(text="Computer Guess", row=2, column=0)
        self.guessDisplay = self.addLabel(
            text="", row=2, column=1)

        self.nextButton = self.addButton(
            text="Next", row=3, column=0, command=self.nextGuess)
        self.newButton = self.addButton(
            text="New game", row=3, column=1, command=self.newGame)
        self.tester = self.addTextArea(
            "", row=4, column=0, columnspan=2, width=20, height=20)

    def nextGuess(self):
        """Processes the computer's next guess."""
        # Get my secret number and disable field
        secretNumber = self.mySecretNumber.getNumber()
        self.mySecretNumber["state"] = "disabled"

        # Display computer's guess
        self.guessDisplay["text"] = str(self.computerGuess)

        # Increase guess count
        self.count += 1

        # Check if guess is correct and give hint when incorrect
        # Display 'win' message and disable next button when guess is correct
        if self.computerGuess == secretNumber:
            self.hintLabel["text"] = "You've guessed it in " + \
                str(self.count) + " attempts!"
            self.nextButton["state"] = "disabled"

        # Display hint when guess is small
        elif self.computerGuess < secretNumber:
            self.hintLabel["text"] = "Sorry, too small!"
            self.tooSmallList.append(self.computerGuess)

            # Get new random guess between largest of tooSmallList to smallest of tooLargeList
            if len(self.tooLargeList) >= 1:
                self.computerGuess = random.randint(
                    max(self.tooSmallList) + 1, min(self.tooLargeList) - 1)
            else:
                if len(self.tooSmallList) == 1:
                    self.computerGuess = random.randint(
                        self.computerGuess + 1, 100)
                else:
                    self.computerGuess = random.randint(
                        max(self.tooSmallList) + 1, 100)

        # Display hint when guess is large
        else:
            self.hintLabel["text"] = "Sorry, too large!"
            self.tooLargeList.append(self.computerGuess)

            # Get new random guess between largest of tooSmallList to smallest of tooLargeList
            if len(self.tooSmallList) >= 1:
                self.computerGuess = random.randint(
                    max(self.tooSmallList) + 1, min(self.tooLargeList) - 1)
            else:
                if len(self.tooLargeList) == 1:
                    self.computerGuess = random.randint(
                        1, self.computerGuess - 1)
                else:
                    self.computerGuess = random.randint(
                        1, min(self.tooLargeList) - 1)

        guessList = self.tooSmallList + self.tooLargeList
        guessList.sort()
        self.tester.setText(str(guessList))

    def newGame(self):
        """Resets the data and GUI to their original states."""
        self.count = 0
        self.hintLabel["text"] = "Guess a number between 1 and 100"
        self.mySecretNumber.setNumber(0)
        self.mySecretNumber["state"] = "normal"
        self.nextButton["state"] = "normal"
        self.computerGuess = random.randint(1, 100)
        self.guessDisplay["text"] = ""
        self.tooSmallList = []
        self.tooLargeList = []
        self.tester.setText("")


def main():
    """Instantiate and pop up the window."""
    ComputerGuessGame().mainloop()


if __name__ == "__main__":
    main()

