import turtle

window = turtle.Screen()
window .bgcolor("black")
window.title("vipin coding")

v=turtle.Turtle()
v.pencolor("white")
v.begin_fill()
v.fillcolor("pink")
v.speed(0)
v.width(8)
v.hideturtle()

# position of design
v.penup()
v.goto(-10,120)
v.pendown()

def curve1():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve2():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve3():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve4():
    for i in range(30):
        v.right(3)
        v.forward(2)

v.forward(80)
curve1()
v.forward(80)
curve2()
v.forward(80)
curve3()
v.forward(80)
curve4()
v.forward(15)

v.penup()
v.right(90)
v.forward(78)
v.pendown()
v.pensize(8)
v.circle(25)

v.penup()
v.left(90)
v.forward(60)
v.left(90)
v.forward(40)
v.pendown()
v.dot(14)
#v.end_fill()
turtle.done()