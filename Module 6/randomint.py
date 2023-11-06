import random

while True:
    # Generate a random integer between 1 and 100
    random_number = random.randrange(1, 100)

    # Check if the random number is odd
    if random_number % 2 == 1:
        # If the number is odd, print it and break out of the loop
        print(random_number)
        break