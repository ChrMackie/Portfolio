def check_sum(num1, num2):
    # Calculate the sum of the two numbers
    total_sum = num1 + num2

    # Check if the sum is greater than 10
    if total_sum > 10:
        print("The sum is greater than 10.")
    # Check if the sum is less than 10
    elif total_sum < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")
# get two inputs from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

check_sum(num1, num2)