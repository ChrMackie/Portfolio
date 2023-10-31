#ChristianMackie
for i in range(1, 51):
  if i % 3 == 0:
    print("Divisible by three")
  elif i % 5 == 0:
    print("Divisible by five")
  elif i % 3 == 0 and i % 5 == 0:
    print("Divisible by both")
  else:
    print(i)
