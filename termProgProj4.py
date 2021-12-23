"""
Program: shapes.py
Author: Ayodele Olufemi
Date: 12/2/2021
Purpose: Initializes the common properties of a geometric shape
"""

import turtle

# Defining the Shapes class


class Shape(turtle.Turtle):
    """Represents a shape superclass, which itself, is a subclass of the Turtle class.
    Specific shapes types inherit from this class."""

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.setheading(0)
        self.width(2)


# Defining the Line class
class Line(Shape):
    def __init__(self):
        super().__init__()

    def draw(self, direction, length):
        self.setheading(direction)
        self.pendown()
        self.forward(length)
        self.hideturtle()


# Defining the Circle class
class Circle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self, x, y, r, fillColor):
        self.goto(x, y)
        self.color(fillColor)
        self.begin_fill()
        self.circle(radius=r)
        self.end_fill()
        self.hideturtle()


# Defining the Rectangle class
class Rectangle(Shape):
    def __init__(self):
        """Creates and instantiates a rectangle."""
        super().__init__()

    def draw(self, x, y, penColor, fillColor, length, width):
        """Draws a rectangle with (x, y) as the coordinate of the top-left corner."""
        self.goto(x, y)
        self.color(penColor, fillColor)
        self.begin_fill()
        self.pendown()
        for i in range(2):
            self.forward(length)
            self.right(90)
            self.forward(width)
            self.right(90)
        self.end_fill()
        self.hideturtle()


# coordinate printer
def buttonclick(x, y):
    print(x, y)


def drawRoof():
    """Draws the house roof."""
    c = Line()
    c.color("bisque3", "burlywood3")
    c.begin_fill()
    c.goto(-740, 371)

    c.draw(25, 200)
    c.draw(13, 225)
    c.draw(347, 50)
    c.draw(0, 750)
    c.draw(323, 200)
    c.draw(180, 500)
    c.draw(160, 270)
    c.draw(200, 270)
    c.draw(20, 240)

    c.goto(-557, 456)

    c.goto(-740, 371)
    c.end_fill()


def drawFacingBoard():
    """Draws the facing board."""
    c = Line()
    c.color("bisque3", "beige")
    c.begin_fill()
    c.goto(-732, 373)
    c.draw(270, 20)
    c.draw(25, 200)
    c.draw(0, 335)
    c.draw(20, 50)
    c.draw(180, 385)
    c.goto(-732, 373)
    c.end_fill()

    d = Line()
    d.color("azure3")
    d.goto(-732, 362)
    d.draw(25, 200)
    d.draw(0, 350)

    e = Line()
    e.color("bisque3", "beige")
    e.begin_fill()
    e.goto(-380, 378)
    e.draw(270, 20)
    e.draw(19, 255)
    e.draw(340, 255)
    e.draw(0, 500)
    e.draw(90, 20)
    e.draw(180, 485)
    e.draw(160, 270)
    e.goto(-380, 378)
    e.end_fill()

    f = Line()
    f.color("azure3")
    f.goto(-381, 367)
    f.draw(20, 255)
    f.draw(340, 270)
    f.draw(0, 490)


def drawWalls():
    """Draws the walls."""
    c = Line()
    c.color("wheat")
    c.begin_fill()
    c.goto(-710, 372)
    c.goto(-552, 449)
    c.goto(-39, 452)
    c.goto(578, 386)
    c.draw(270, 800)
    c.goto(-710, -414)
    c.goto(-710, 372)
    c.end_fill()

def drawWallLines():
    """Draws the house wall coverings."""
    i = Line()
    i.color("burlywood4")
    i.goto(-711, -393)
    for k in range(13):
        i.draw(0, 1290)
        i.penup()
        i.left(90)
        i.forward(30)
        i.left(90)
        i.draw(180, 1290)
        i.penup()
        i.right(90)
        i.forward(30)
    i.penup()
    i.goto(-681, 382)
    i.draw(0, 370)
    i.penup()
    i.goto(-608, 410)
    i.draw(0, 370)

def drawWindows():
    """Draws the left and right windows."""
    # Left windows
    c = Rectangle()
    c.draw(-690, 295, "bisque3", "AntiqueWhite2", 200, 500)
    c.draw(-690, 40, "bisque3", "AntiqueWhite4", 200, 250)
    c.penup()
    c.draw(-702, -203, "cyan4", "cyan4", 222, 25)
    
    g = Line()
    g.color("burlywood4")
    g.penup()
    g.pensize(3)
    g.goto(-691, 171)
    g.draw(0, 200)
    g.penup()
    g.goto(-491, 237)
    g.draw(180, 200)
    g.penup()
    c.penup()
    c.draw(-600, 296, "AntiqueWhite4", "wheat", 15, 258)
    g.pensize(3)
    g.goto(-648, 296)
    g.draw(270, 125)
    g.penup()
    g.goto(-541, 296)
    g.draw(270, 125)

    # Right windows
    d = Rectangle()
    d.draw(160, 295, "bisque3", "AntiqueWhite2", 400, 500)
    d.draw(160, 40, "bisque3", "AntiqueWhite4", 400, 250)
    d.penup()
    d.draw(152, -203, "cyan4", "cyan4", 415, 25)
    g.penup()
    g.goto(159, 171)
    g.draw(0, 400)
    g.penup()
    g.goto(160, 237)
    g.draw(0, 400)
    g.penup()
    g.goto(212, 296)
    g.draw(270, 125)
    g.penup()
    g.goto(350, 296)
    g.draw(270, 125)
    g.penup()
    g.goto(494, 296)
    g.draw(270, 125)
    c.penup()
    c.draw(273, 296, "AntiqueWhite4", "wheat", 15, 258)
    c.penup()
    c.draw(416, 296, "AntiqueWhite4", "wheat", 15, 258)
    
def houseNumber():
    """Draws the house number."""
    turtle.penup()
    turtle.goto(95, 115)
    turtle.write("123", font=("Miriam", 20, "normal"))
    turtle.hideturtle()



def drawPillars():
    """Draws the two house pillars."""
    e = Rectangle()
    e.draw(-366, 360, "bisque3", "brown4", 40, 776)

    f = Rectangle()
    f.draw(37, 360, "bisque3", "brown4", 40, 776)

def drawFrontTop():
    """Draws the top front part of the building."""
    g = Line()
    g.color("beige")
    g.begin_fill()
    g.goto(-368, 360)
    g.goto(-138, 439)
    g.goto(77, 362)
    g.goto(-368, 360)
    g.end_fill()
    g.hideturtle()

    h = Line()
    h.color("wheat")
    h.begin_fill()
    h.goto(-240, 404)
    h.goto(-138, 440)
    h.goto(-40, 404)
    h.goto(-240, 404)
    h.end_fill()
    h.hideturtle()

def drawDoor():
    """Draws the house door."""
    k = Rectangle()
    k.draw(-278, 216, "beige", "white", 275, 530)
    k.penup()
    k.draw(-246, 183, "cyan4", "cyan4", 210, 497)
    l = Circle()
    l.draw(-233, -114, 10, "black")
    k.penup()
    k.draw(-233, -103, "black", "black", 15, 5)

def drawGrass():
    """Draws the grasses around the building."""
    t = Rectangle()
    t.draw(-1554, -415, "limegreen", "limegreen", 4000, 500)

def drawStairs():
    """Draws the front stairs by stairway."""
    f = Rectangle()
    f.draw(-326, -308, "brown4", "brown4", 365, 105)
    g = Line()
    g.goto(-327, -344)
    g.color("wheat")
    g.pensize(4)
    g.draw(0, 365)
    g.penup()
    g.right(90)
    g.forward(25)
    g.draw(180, 365)
    g.penup()
    g.left(90)
    g.forward(25)
    g.draw(0, 365)
    g.penup()
    g.goto(-295, -344)
    g.pensize(2)
    for e in range(4):
        g.draw(270, 23)
        g.left(90)
        g.forward(40)
        g.left(90)
        g.draw(90, 23)
        g.right(90)
        g.forward(40)
    g.penup()
    g.goto(-285, -369)
    for e in range(4):
        g.draw(270, 23)
        g.left(90)
        g.forward(40)
        g.left(90)
        g.draw(90, 23)
        g.right(90)
        g.forward(40)

def drawStickFigure():
    """Draws a stick figure opening the door."""
    c = Circle()
    c.penup()
    c.draw(-275, 0, 30, "black")
    d = Line()
    d.color("black")
    d.pensize(8)
    d.penup()
    d.goto(-274, 7)
    d.draw(268, 250)
    d.draw(240, 75)
    d.penup()
    d.goto(-281, -225)
    d.draw(350, 15)
    d.draw(280, 70)
    d.penup()
    d.goto(-275, -53)
    d.pendown()
    d.goto(-254, -128)
    d.goto(-236, -104)
    d.penup()
    d.goto(-275, -53)
    d.pendown()
    d.goto(-318, -67)
    d.goto(-236, -103)
    
def drawWalkWay():
    """Draws the walkway."""
    c = Line()
    c.goto(-365, -415)
    c.color("cornsilk4")
    c.begin_fill()
    c.draw(0, 440)
    c.draw(200, 100)
    c.draw(260, 400)
    c.draw(180, 110)
    c.draw(100, 400)
    c.goto(-365, -415)
    c.end_fill()
    c.penup()
    c.goto(-208, -787)
    c.color("burlywood3")
    c.draw(0, 127)
    c.penup()
    c.goto(-233, -646)
    c.draw(0, 185)
    c.penup()
    c.goto(-268, -448)
    c.pendown()
    c.goto(-19, -449)

def drawMailbox():
    """Draws the mailbox."""
    d = Rectangle()
    d.draw(-467, 49, "black", "black", 80, 15)

def drawClouds():
    """Draws some clouds in the sky. """
    g = Circle()
    g.draw(443, 639, 80, "CadetBlue1")
    g.penup()
    g.draw(500, 641, 50, "CadetBlue1")
    g.penup
    g.draw(390, 622, 70, "CadetBlue1")


# Main method
def main():
    wn = turtle.Screen()
    wn.title("Turtle house and stick figure")
    wn.bgcolor("CadetBlue3")

    drawGrass()
    drawWalls()
    drawWallLines()
    drawRoof()
    drawFacingBoard()
    drawFrontTop()
    drawWindows()
    drawDoor()
    drawStairs()
    drawPillars()
    houseNumber()
    drawMailbox()
    drawStickFigure()
    drawWalkWay()
    drawClouds()

    wn.exitonclick()


if __name__ == "__main__":
    main()

