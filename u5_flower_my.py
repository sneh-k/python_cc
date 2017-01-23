import turtle

window=turtle.Screen()

turtle_name= turtle.Turtle()
turtle_name.speed(50)
for j in range(1,37):
    turtle_name.color("blue")
    for i in range(1, 3):
        if i%2==0:
           turtle_name.color("red")
        turtle_name.back(50)
        turtle_name.right(20)
        if i % 2 == 1:
           turtle_name.color("red")
        else:
           turtle_name.color("blue")
        turtle_name.back(50)
        turtle_name.right(160)
        turtle_name.color("blue")
    turtle_name.right(10)

turtle_name.color("black")
turtle_name.right(90)
turtle_name.forward(300)
window.exitonclick()