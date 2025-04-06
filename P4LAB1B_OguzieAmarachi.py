import turtle

t = turtle.Turtle()
t.color("blue")    
t.pensize(5)
t.speed(2)

t.penup()
t.goto(-50, 0)
t.pendown()
t.circle(50)

t.penup()
t.goto(100, 0)
t.setheading(0)
t.pendown()

t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(50)
t.right(105)
t.forward(30)

turtle.done()
