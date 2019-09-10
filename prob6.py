d = 0
for x in range(1,101):
  for y in range(x+1, 101):
    d += 2*x*y

print(d)

# Note: I worked out by hand that the difference between the sum of the squares and the square of the sum is 2*(a*b + a*c + b*c + ...).