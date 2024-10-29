"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()
tina.shape("turtle")
                 # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

sides = 6
angle = 360/sides

angle

for i in range(sides):
    tina.forward(150)
    tina.left(angle)
    

    tina.penup()
    tina.forward(75)
    tina.left(90)
    tina.forward(150)


turtle.exitonclick()                    # Close the window when we click on it
