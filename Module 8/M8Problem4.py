def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False

#taking year as input from the user
year_input = int(input("Enter a year: "))
result = is_leap_year(year_input)
if result:
        print(f"{year_input} is a leap year")
else:
        print(f"{year_input} is not a leap year")