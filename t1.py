import turtle

t = turtle.Turtle()
t.speed(3)


t.color("red")
for i in range(4):
    t.forward(100)
    t.left(90)


t.penup()
t.goto(150, 0)
t.pendown()

t.color("blue")
for i in range(36):
    t.forward(10)
    t.left(10)


t.penup()
t.goto(-150, 0)
t.pendown()


t.color("green")
for i in range(6):
    t.forward(80)
    t.left(60)

turtle.done()
