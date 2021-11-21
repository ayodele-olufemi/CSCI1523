"""
Program: 20211108_03
Author: Ayodele Olufemi
Date: 11/08/2021
"""

from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label and buttons."""
        EasyFrame.__init__(self, title = "Button Demo")

        # A single label in the first row.
        self.label = self.addLabel(text = "Hello World!", row = 0, column = 0, columnspan = 2, sticky = "NSEW")

        # Two command buttons in the second row. 
        self.clearBtn = self.addButton(text = "Clear", row = 1, column = 0, command = self.clear)
        self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 1, command  = self.restore, state = "disabled")

    # Methods to handle user events. 
    def clear(self):
        """Resets the label to the empty string and the button states."""
        self.label["text"] = ""
        self.clearBtn["state"]= "disabled"
        self.restoreBtn["state"] = "normal"

    def restore(self):
        """Resets the label to 'Hello World!' and sets teh state of the buttons."""
        self.label["text"] = "Hello World!"
        self.clearBtn["state"] = "normal"

def main():
    """Instantiate and pop up the window."""
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()


