"""
Program: 20211115_CheckbuttonDemo
Author: Ayodele Olufemi
Date: 11/15/2021
Purpose: Demonstrate the use of dialog box class within out Python GUI application.
"""

from breezypythongui import EasyFrame


class CheckbuttonDemo(EasyFrame):
    """Allows the use to place a restaurant order from a set of options."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Check Button Demo")

        # Add four check buttons
        self.chickCB = self.addCheckbutton(text="Chicken", row=0, column=0)
        self.taterCB = self.addCheckbutton(
            text="French fries", row=0, column=1)
        self.beanCB = self.addCheckbutton(text="Green beans", row=1, column=0)
        self.sauceCB = self.addCheckbutton(text="Applesauce", row=1, column=1)
        self.addButton(text="Place order", row=2, column=0,
                       columnspan=2, command=self.placeOrder)

    # Event handle method
    def placeOrder(self):
        """Display a message box with the order information"""
        message = ""
        if self.chickCB.isChecked():
            message += "Chicken\n\n"
        if self.taterCB.isChecked():
            message += "French fries\n\n"
        if self.beanCB.isChecked():
            message += "Green beans\n\n"
        if self.sauceCB.isChecked():
            message += "Applesauce\n"
        if message == "":
            message = "No food ordered!"
        self.messageBox(title="Customer Order", message=message)


def main():
    """Instantiate and pop up the window."""
    CheckbuttonDemo().mainloop()


if __name__ == "__main__":
    main()

