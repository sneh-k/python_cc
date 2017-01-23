import turtle


def draw_sq():
#    window.bgcolor("light blue")

    teddy=turtle.Turtle()
    teddy.shape("turtle")
    teddy.color("red")
    #teddy.speed(10)

    for i in range(1,5):
        teddy.back(100)
        teddy.right(90)
        i+=1

def draw_cr():

    pooh=turtle.Turtle()
    pooh.shape("arrow")
    pooh.color("blue")
    pooh.circle(25)

def draw_tr():
    vinnie = turtle.Turtle()
    vinnie.shape("classic")
    vinnie.color("orange")

    for i in range(1,4):
        vinnie.forward(100)
        vinnie.left(120)
        i+=1

window=turtle.Screen()
draw_tr()
draw_cr()
draw_sq()
window.exitonclick()