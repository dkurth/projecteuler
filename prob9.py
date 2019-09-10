import math

for a in range(1,500):
  for b in range(1,500):
    c = math.sqrt(a*a + b*b)
    if a + b + c == 1000:
      print("{}, {}, {}".format(a, b, c))