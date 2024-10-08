"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


tina.color("red")
tina.forward(50)
tina.left(60)

tina.color("orange")
tina.forward(50)
tina.left(60)

tina.color("yellow")
tina.forward(50)
tina.left(60)

tina.color("green")
tina.forward(50)
tina.left(60)

tina.color("blue")
tina.forward(50)
tina.left(60)

tina.color("purple")
tina.forward(50)
tina.left(60)

tina.right(90)
tina.penup()
tina.forward(50)
tina.pendown()

for i in range(4):
   print('Loop Iteration', i)



turtle.exitonclick()                    # Close the window when we click on it
