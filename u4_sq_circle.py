import turtle


def draw_sq(turtle_name):
    for i in range(1,5):
        turtle_name.back(100)
        turtle_name.right(90)

def draw():
    window=turtle.Screen()
    window.bgcolor("yellow")

    teddy=turtle.Turtle()
    teddy.shape("classic")
    teddy.color("red")
    teddy.speed(10)
    for i in range(1,37):
        draw_sq(teddy)
        teddy.right(10)
    window.exitonclick()

draw()