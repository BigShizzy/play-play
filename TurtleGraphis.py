import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")


colors = ["red", "yellow", "blue", "green", "orange", "purple"]

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i * 1.5)
    t.left(59)
    t.width(i / 100 + 1)

turtle.done()