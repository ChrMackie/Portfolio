# initialize the total sum to 0
total_sum = 0
# initialize an empty list to store the entered numbers
number_list = []

#loop condition
while total_sum <= 100:
    # enter a number
    user_number = int(input("Enter a number: "))

    # add the entered number to the list
    number_list.append(user_number)

    # update the total sum by adding the entered number
    total_sum += user_number

print("The list of numbers is:", number_list)
print("The total sum of the numbers is:", total_sum)