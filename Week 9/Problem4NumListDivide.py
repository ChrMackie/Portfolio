tens = []
counter = 0

#loop until counter reaches 50
while counter <= 50:
    # checks if current counter is divisible by 10
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(tens)