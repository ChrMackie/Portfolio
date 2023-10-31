import turtle

# Ask the user for the number of sides, the length of the side, the color of the line, and the fill color of the polygon.
sides = int(input("Enter the number of sides: "))
side_length = float(input("Enter the length of the side: "))
line_color = input("Enter the color of the line: ")
fill_color = input("Enter the fill color: ")

# Set the turtle's color and fill color.
turtle.color(line_color)
turtle.fillcolor(fill_color)

# Begin filling the polygon.
turtle.begin_fill()

# Draw the polygon.
for i in range(sides):
  turtle.forward(side_length)
  turtle.left(360 / sides)

# End filling the polygon.
turtle.end_fill()

turtle.hideturtle()

turtle.done()
