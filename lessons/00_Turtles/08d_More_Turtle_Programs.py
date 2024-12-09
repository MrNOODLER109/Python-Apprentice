"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""
import turtle                           
turtle.setup (width=600, height=600)    

tina = turtle.Turtle()                  

tina.begin_fill()

tina.forward(100)
tina.left(45)
tina.forward(50)
tina.left(135)
tina.forward(165)
tina.left(135)
tina.forward(50)

tina.end_fill()

tina.undobufferentries()

turtle.exitonclick()