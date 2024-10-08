
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""



import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape('turtle')

tina.color("cyan")
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(10)
tina.right(90)
tina.forward(10)
tina.right(90)
tina.forward(10)
tina.right(90)
tina.forward(5)
tina.left(90)
tina.forward(10)
tina.left(90)
tina.forward(5)
tina.right(90)
tina.forward(10)
tina.right(90)
tina.forward(5)
tina.left(90)
tina.forward(10)
tina.left(90)
tina.forward(5)
tina.right(90)
tina.forward(10)
tina.right(90)
tina.forward(10)



turtle.exitonclick()


