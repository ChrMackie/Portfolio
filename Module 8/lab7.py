import turtle

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

#set up the turtle screen
turtle.speed(0)
turtle.bgcolor("black")
turtle.color("white")

#adjust these parameters to create a pattern
num_polygons = 20 #number of polygons to draw
polygon_sides = 8 #number of sides in each polygon
side_length = 35 #lenghth of each side

#draw the pattern
for i in range(num_polygons):
    draw_polygon(polygon_sides, side_length)
    turtle.right(360 / num_polygons)

# close the turtle graphics window
turtle.done()