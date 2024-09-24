"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.speed(0.75)
tina.pencolor('red')
tina.begin_fill()
tina.circle(100)
tina.end_fill()
tina.right(80)
tina.forward(50)
tina.write("     I am Tina, Lord of the Black Sun.")

tina.right(10)
tina.forward(25)

import turtle

bob = turtle.Turtle()
bob.speed(0.5)
bob.right(90)
bob.pendown()
bob.forward(100)

bob.write("      I am Bob., Hi!")
tina.write("    Bob, SPIN, SPIN, SPIN! HAHAHAHAHA")
bob.speed(10)
bob.right(150000)



turtle.exitonclick()                    # Close the window when we click on it
