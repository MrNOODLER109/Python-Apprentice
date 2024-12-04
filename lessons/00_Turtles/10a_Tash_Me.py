""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spot on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

t = turtle.Turtle()                  # Create a turtle named tina

t.shape('turtle')                    # Set the shape of the turtle to a turtle
t.speed(2) 
                          

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")

# This is the function that gets called when you click on the screen
def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open






