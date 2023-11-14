# Christian Mackie 11/12/2023
def multiply_list(numbers):
  total = 1

  # Iterate through each number in the list
  for number in numbers:
    # Multiply the current number with the total
    total *= number

  # return final product
  return total

# Multiply the numbers in the list [5, 2, 7, -1]
numbers = [5, 2, 7, -1]
result = multiply_list(numbers)
print(result)