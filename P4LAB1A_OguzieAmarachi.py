import turtle

t = turtle.Turtle()
t.speed(2)

for _ in range(4):
    t.forward(100)
    t.right(90)

sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

turtle.done()
