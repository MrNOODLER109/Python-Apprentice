""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

def set_turtle_image(turtle, leaguebot_bolt):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / leaguebot_bolt)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


screen = turtle.Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor('white')

t = turtle.Turtle()


set_turtle_image(t, "leaguebot_bolt.gif")
turtle.shapesize(10, 10)
t.color("blue")

sides = 6
angle = 360/sides

angle

for sides in range(1, 10):
    angle = ...
    print("Angle for ", sides, " sides is ", angle)

turtle.exitonclick()