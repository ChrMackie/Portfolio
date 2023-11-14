import math

def areaOfCircle(r):
    # Calculate the area of the circle using the formula pi * r ^ 2
    area = math.pi * r * r

    # Return the calculated area
    return area

# Example usage
radius = 5
area = areaOfCircle(radius)
print("The area of a circle with radius", radius, "is:", area)