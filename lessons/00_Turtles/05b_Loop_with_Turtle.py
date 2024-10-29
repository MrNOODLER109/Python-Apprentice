
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

tina.forward(200)
tina.left(90)

tina.forward(200)
tina.left(90)

tina.forward(200)
tina.left(90)

tina.forward(200)
tina.left(90)

tina.forward(100)
tina.left(90)
tina.penup()
tina.forward(100)

tina.write("                                    This is the arena!")

import turtle
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(2)
bob.penup()

bob.forward(100)
bob.left(90)
bob.forward(50)

tina.forward(50)
tina.right(180)

bob.write("                                     We will fight!")

bob.forward(95)

tina.left(360)

bob.right(360)
bob.back(95)

tina.forward(95)

bob.left(360)

tina.right(360)
tina.back(95)

bob.left(90)
bob.forward(50)
bob.right(90)
bob.forward(95)
bob.right(90)
bob.forward(50)

tina.left(360)

bob.right(360)
bob.left(90)
bob.back(95)

tina.left(90)
tina.forward(50)
tina.right(90)
tina.forward(95)
tina.right(90)
tina.forward(50)

bob.left(360)

tina.right(360)
tina.left(90)
tina.back(95)

import turtle
kingg = turtle.Turtle()
kingg.color("red")
kingg.shape("turtle")
kingg.speed(2)
kingg.penup()


kingg.left(90)
kingg.forward(100)
kingg.right(90)
kingg.write("       I am King Galbatorix, prepare to die!")

tina.write("    No!")
bob.write("     No, please!")
tina.hideturtle()
bob.hideturtle()

turtle.done()












                                            
turtle.exitonclick()                    # Close the window when we click on it
