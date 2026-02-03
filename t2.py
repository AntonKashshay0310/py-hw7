import turtle

screen = turtle.Screen()
screen.tracer(1)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(1)

colors = ["red", "yellow", "green", "yellow"]

for color in colors:
    t.clear()
    t.goto(0, 0)
    t.color(color)
    t.pendown()

    
    for i in range(4):
        t.forward(50)
        t.right(90)

    t.penup()
    screen.update()

turtle.done()
