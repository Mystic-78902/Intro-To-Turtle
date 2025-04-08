
import turtle
import time


screen = turtle.Screen()
screen.title("Geometric Shapes")
screen.bgcolor("lightblue")  

t = turtle.Turtle()
t.speed(2) 
t.pensize(3)  

def draw_triangle():
    t.color("red")
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

def draw_rectangle():
    t.color("blue")
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

def draw_hexagon():
    t.color("purple")
    t.fillcolor("pink")
    t.begin_fill()
    for _ in range(6):
        t.forward(70)
        t.left(60)
    t.end_fill()

t.penup()
t.goto(-200, 0)  
t.pendown()
draw_triangle()

t.penup()
t.goto(0, 0)  
t.pendown()
draw_rectangle()

t.penup()
t.goto(200, 0) 
t.pendown()
draw_hexagon()

t.hideturtle()
screen.mainloop()
