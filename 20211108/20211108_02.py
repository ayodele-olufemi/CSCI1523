"""
Program: 20211108_02
Author: Ayodele Olufemi
Date: 11/08/2021
Purpose: A simple application which demostrates positioning and layout on a GUI
File: layoutdemo.py
"""

from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    """Displays labels in the quandrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0)
        self.addLabel(text = "(0, 1)", row = 0, column = 1)
        self.addLabel(text = "(1, 0)", row = 1, column = 0)
        self.addLabel(text = "(1, 1)", row = 1, column = 1)

def main():
    """Instantiates and pops up the window."""
    LayoutDemo().mainloop()

if __name__ == "__main__":
    main()


