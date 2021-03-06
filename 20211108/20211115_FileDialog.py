"""
Program: 20211115_FileDialog
Author: Ayodele Olufemi
Date: 11/15/2021
Purpose: Demonstrate the use of dialog box class within out Python GUI application.
"""

from breezypythongui import EasyFrame
import tkinter.filedialog


class FileDialogDemo(EasyFrame):
    """Demonstrates the use of a file dialog."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "File Dialog Demo")
        self.outputArea = self.addTextArea(
            "", row=0, column=0, width=80, height=15)
        self.addButton(text="Open", row=1, column=0, command=self.openFile)

    # Event Handling Method:
    def openFile(self):
        """Pops up and open file dialog, and if a file is selected, displays the text in the text area and its pathname in the title bar."""
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]
        fileName = tkinter.filedialog.askopenfilename(
            parent=self, filetypes=fList)

        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)


def main():
    """Instantiate and pop up the window."""
    FileDialogDemo().mainloop()


if __name__ == "__main__":
    main()

