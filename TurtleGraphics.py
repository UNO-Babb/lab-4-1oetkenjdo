#TurtleGraphics.py
#Name: Jacob Oetken
#Date: 2/15/25
#Assignment: LAB 4

import turtle #needed generally but not in CodeHS


def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    angle = 360 / sides
    for _ in range(sides):
        myTurtle.forward(50)
        myTurtle.right(angle)


def fillCorner(myTurtle, corner):  
    if corner == 2:
        myTurtle.up()
        myTurtle.home()
        myTurtle.down()
        drawSquare(myTurtle, 100)
        myTurtle.fillcolor("red")
        myTurtle.begin_fill()
        myTurtle.forward(100)
        for i in range(3):
            myTurtle.right(90)
            myTurtle.forward(50)
        myTurtle.end_fill()
    if corner == 3:
        myTurtle.up()
        myTurtle.home()
        myTurtle.down()
        drawSquare(myTurtle, 100)
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.fillcolor("red")
        myTurtle.begin_fill()
        for i in range (3):
            myTurtle.left(90)
            myTurtle.forward(50)
        myTurtle.end_fill()

def squaresInSquares(myTurtle, count):
    factor = 2
    x = -40
    y = 40
    size = 100
    myTurtle.up()
    myTurtle.goto(x,y)
    myTurtle.down()
    for i in range(count):
        drawSquare(myTurtle, size)
        x = x * (2 / factor)
        y = y * (2 / factor)
        y -= 10
        x += 10
        myTurtle.up() 
        myTurtle.goto(x, y)
        myTurtle.down()
        size += 20

    
def main():
    myTurtle = turtle.Turtle()
            #Uncomment one of the following lines to test:
    #drawPolygon(myTurtle, 5)  # Draws a pentagon
    #drawPolygon(myTurtle, 8)  # Draws an octagon

    #fillCorner(myTurtle, 2)   # Draws a square with the top right corner filled
    #fillCorner(myTurtle, 3)   # Draws a square with the bottom left corner filled   

    #squaresInSquares(myTurtle, 5)  # Draws 5 concentric squares #FOR SOME REASON, THESE CANT RUN SEQUENTIALLY WITH THE OTHER COMMANDS...
    #squaresInSquares(myTurtle, 3)  # Draws 3 concentric squares #FOR SOME REASON, THESE CANT RUN SEQUENTIALLY WITH THE OTHER COMMANDS... 

    #after 2 hours of work and coordination with my buddy in cybersecurity, it now works sequentially. :)

main()




#old squaresinsquares

#def squaresInSquares(myTurtle, count):
#    size = 100
#    myTurtle.up()
#    myTurtle.goto(-40,40)
#    myTurtle.down()
#    for i in range(count):
#        drawSquare(myTurtle, size)
#        myTurtle.up() 
#        myTurtle.goto(-size/2, size/2)
#        myTurtle.down()
#        size += 20
