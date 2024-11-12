"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""


import turtle                           
turtle.setup (width=600, height=600)    

tina = turtle.Turtle()                  

tina.shape('turtle')                   
tina.speed(2)
tina.shapesize(5)

tina.penup()
tina.forward(200)
tina.left(90)
tina.pendown()
tina.back(200)

import turtle                           
turtle.setup (width=600, height=600)    

a = turtle.Turtle()                  

a.shape('turtle')

import turtle                           
turtle.setup (width=600, height=600)    

b = turtle.Turtle()                  

b.shape('turtle') 

import turtle                           
turtle.setup (width=600, height=600)    

c = turtle.Turtle()                  

c.shape('turtle')

import turtle                           
turtle.setup (width=600, height=600)    

d = turtle.Turtle()                  

d.shape('turtle') 

a.penup()
a.left(90)
a.forward(100)

b.penup()
b.forward(100)

c.penup()
c.right(90)
c.forward(100)

d.penup()
d.right(180)
d.forward(100)

for i in range(50):
    tina.forward(400)
    tina.left(90)
    print('Loop Iteration', i)

    import turtle                           
turtle.setup (width=600, height=600)    

bob = turtle.Turtle()                  

bob.shape('turtle')                   
bob.speed(2)
bob.shapesize(10)

bob.pencolor("lavender")
bob.color("light blue")

bob.write("                                                                         I am Big Bob")
b.hideturtle()
bob.left(90)
a.hideturtle()
bob.left(90)
d.hideturtle()
bob.left(90)






turtle.exitonclick()
