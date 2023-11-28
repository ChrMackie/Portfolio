import turtle

#create turtle screen
screen=turtle.Screen()
screen.bgcolor("black")

#create a turtle
pen= turtle.Turtle()
pen.speed(5)
pen.color("blue")
pen.pensize(2)

#fucnrion to draw a hexagon

def draw_hexagon():
    for _ in range(6):
        pen.forward(50)
        pen.left(60)

#draw two hexagons side by side
for _ in range(9):
    draw_hexagon()
    #pen.penup()
    pen.left(80) #move tp the right for the next hexagon
    #pen.pendown()

#close turtle graphics window
turtle.done()