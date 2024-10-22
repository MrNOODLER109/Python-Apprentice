""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 60 # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(150)                             # Move tina forward by the forward distance
        tina.left(sides)                              # Turn tina left by the left turn


draw_polygon(sides)                        # Draw a square

...                                      # Move tina to another spot on the screen

draw_polygon(...)                        # Draw a pentagon

...                                      # Move tina to another spot on the screen

draw_polygon(...)                        # Draw a hexagon


turtle.exitonclick()                     # Close the window when we click on it # Your code here

