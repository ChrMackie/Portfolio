def is_in_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False

# Check if 5 is in the range 1 to 10
if is_in_range(5, 1, 10):
    print("5 is in the range 1 to 10")
else:
    print("5 is not in the range 1 to 10")