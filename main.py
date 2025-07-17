import turtle
import colorsys

turtle.bgcolor("black")
turtle.tracer(100)
turtle.pensize(1)
h = 0.5
for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    h = 0.0008
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.fd(i)
    turtle.lt(100)
    turtle.circle(30)
    for j in range(2):
        turtle.fd(i*j)
        turtle.rt(109)
    turtle.end_fill()
my_screen = turtle.Screen()
my_screen.exitonclick()
