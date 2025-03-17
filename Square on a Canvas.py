import turtle

turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(2):
    board.forward(100)
    board.left(90)
    board.forward(60)
    board.left(90)
turtle.done()