def machin_like_formula():
  # Calculate pi using the Machin-like formula
  pi = 4 * (1 - 1/5 - 1/239)
  return pi

pi_approx = machin_like_formula()

print("Machin-like formula approximation of pi:", pi_approx)
print("Math module value of pi:", math.pi)