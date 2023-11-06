import math

# user to enter a number
user_input_number = int(input("Enter a number: "))

# Calculate the factorial using a for loop
factorial = 1
for i in range(1, user_input_number + 1):
    factorial *= i

# Calculate the factorial using the math module's factorial function
math_factorial = math.factorial(user_input_number)

# Print the factorial values
print("Factorial using for loop:", factorial)
print("Factorial using math module:", math_factorial)